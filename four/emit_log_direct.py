import sys
from channel import (
    channel_connection,
    connection,
    exchange_name,
)


severity = sys.argv[1] if len(sys.argv) > 1 else "info"
message = " ".join(sys.argv[2:]) or "Hello World!"
channel_connection.basic_publish(
    exchange=exchange_name, routing_key=severity, body=message
)
print(f" [x] Sent {severity}: {message}")
connection.close()
