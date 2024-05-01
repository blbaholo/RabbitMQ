import pika
import sys
from channel import (
    connection,
    channel_connection,
    queue_name,
)


message = " ".join(sys.argv[1:]) or "Hello World!"
channel_connection.basic_publish(
    exchange="",
    routing_key=queue_name,
    body=message,
    properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE),
)
print(f" [x] Sent {message}")
connection.close()
