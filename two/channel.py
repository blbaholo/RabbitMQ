import pika
import os

host = os.getenv("HOST", "localhost")
queue_name = "task_queue"
connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
channel_connection = connection.channel()
channel_connection.queue_declare(queue=queue_name, durable=True)
