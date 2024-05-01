import pika
import uuid
from channel import connection, queue_name, channel_connection


class FibonnaciRpcClient:
    def __init__(self):
        self.connection = connection
        self.channel = channel_connection
        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True,
        )
        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange="",
            routing_key=queue_name,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n),
        )
        self.connection.process_data_events(time_limit=None)
        return int(self.response)


if __name__ == "__main__":
    fibonnaci_rpc = FibonnaciRpcClient()
    print(f" [x] Requesting fib(30)")
    response = fibonnaci_rpc.call(30)
    print(f" [.] Got {response}")