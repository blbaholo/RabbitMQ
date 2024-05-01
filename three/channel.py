import pika
import os

host = os.getenv("HOST", "localhost")
exchange_name = "logs"
connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
channel_connection = connection.channel()
channel_connection.exchange_declare(exchange=exchange_name, exchange_type="fanout")
