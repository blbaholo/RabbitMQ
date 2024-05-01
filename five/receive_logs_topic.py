import sys
import os
from channel import channel_connection, exchange_name


def main():
    result = channel_connection.queue_declare("", exclusive=True)
    queue_name = result.method.queue

    binding_keys = sys.argv[1:]
    if not binding_keys:
        sys.stderr.write(f"Usage: {sys.argv[0]} [binding_key]...\n")
        sys.exit(1)

    for binding_key in binding_keys:
        channel_connection.queue_bind(
            exchange=exchange_name, queue=queue_name, routing_key=binding_key
        )

    print(" [*] Waiting for logs, To exit press CTRL+C")

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
