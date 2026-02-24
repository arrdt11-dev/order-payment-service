import json
import pika

def publish_order_created(order: dict):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    )
    channel = connection.channel()

    channel.queue_declare(queue="order_created")

    channel.basic_publish(
        exchange="",
        routing_key="order_created",
        body=json.dumps(order)
    )

    connection.close()
