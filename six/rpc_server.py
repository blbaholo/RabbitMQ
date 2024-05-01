import pika
import sys
import os
from channel import channel_connection, queue_name


def main():
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    def on_request(ch, method, props, body):
        n = int(body)
        print(f" [.] fib({n})")
        response = fib(n)
        ch.basic_publish(
            exchange="",
            routing_key=props.reply_to,
            properties=pika.BasicProperties(correlation_id=props.correlation_id),
            body=str(response),
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel_connection.basic_qos(prefetch_count=1)
    channel_connection.basic_consume(queue=queue_name, on_message_callback=on_request)
    print(" [x] Awaiting RPC requests")
    channel_connection.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
