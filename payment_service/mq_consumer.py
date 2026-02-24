import json
import pika

def callback(ch, method, properties, body):
    order = json.loads(body)

    print("Received order:", order)

    if order["amount"] > 0:
        status = "paid"
    else:
        status = "failed"

    print(f"Payment result: {status}")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)

channel = connection.channel()
channel.queue_declare(queue="order_created")

channel.basic_consume(
    queue="order_created",
    on_message_callback=callback,
    auto_ack=True
)

print("Waiting for orders...")
channel.start_consuming()
