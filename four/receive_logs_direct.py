import sys
import os
from channel import channel_connection, exchange_name


def main():
    result = channel_connection.queue_declare(queue="", exclusive=True)
    queue_name = result.method.queue

    severities = sys.argv[1:]
    if not severities:
        sys.stderr.write(f"Usage: {sys.argv[0]} [info] [warning] [error]\n")
        sys.exit(1)

    for severity in severities:
        channel_connection.queue_bind(
            exchange=exchange_name, queue=queue_name, routing_key=severity
        )

    print(" [*] Waiting for logs. To exit press CTRL+C")

    def callback(ch, method, properties, body):
        print(f" [x] {method.routing_key}: {body}")

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