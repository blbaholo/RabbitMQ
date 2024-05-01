import os
import sys
from channel import channel_connection, exchange_name


def main():
    result = channel_connection.queue_declare(queue="", exclusive=True)
    queue_name = result.method.queue
    channel_connection.queue_bind(exchange=exchange_name, queue=queue_name)
    print(" [*] Waiting for logs. To exit press CTRL+C")

    def callback(ch, method, properties, body):
        print(f" [x] {body}")

    channel_connection.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
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