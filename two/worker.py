import time
import os
import sys
from channel import channel_connection, queue_name


def main():
    print(" [*] Waiting for messages. To exit press CTRL+C")

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b"."))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel_connection.basic_qos(prefetch_count=1)
    channel_connection.basic_consume(queue=queue_name, on_message_callback=callback)
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