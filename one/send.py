from channel import (
    connection,
    channel_connection,
    queue_name,
)

message = "Hello World"
channel_connection.basic_publish(exchange="", routing_key=queue_name, body=message)
print(f" [x] Sent {message}")
connection.close()
