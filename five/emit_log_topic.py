import sys
from channel import (
    channel_connection,
    connection,
    exchange_name,
)


routing_key = sys.argv[1] if len(sys.argv) > 2 else "anonymous.info"
message = " ".join(sys.argv[2:]) or "Hello World!"
channel_connection.basic_publish(
    exchange=exchange_name, routing_key=routing_key, body=message
)
print(f" [x] Sent {routing_key}: {message}")
connection.close()
