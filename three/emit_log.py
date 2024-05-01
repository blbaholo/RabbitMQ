import sys
from channel import (
    connection,
    channel_connection,
    exchange_name,
)


message = " ".join(sys.argv[1:]) or "info: Hello World!"
channel_connection.basic_publish(exchange=exchange_name, routing_key="", body=message)
print(f" [x] Sent {message}")
connection.close()
