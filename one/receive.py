import sys
import os
from channel import queue_name, channel_connection


def main():
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel_connection.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True
    )
    print(" [*] Waiting for messages. To exit press CTRL+C")
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
