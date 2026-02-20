import pika
import json
import time

# Подключаемся к RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='order_queue')

def process_order(ch, method, properties, body):
    data = json.loads(body)
    print(f" [MQ] Получен заказ {data['order_id']} на сумму {data['amount']}")
    
    # Имитация работы
    time.sleep(2)
    
    status = "success" if data['amount'] > 0 else "failed"
    print(f" [MQ] Результат оплаты для заказа {data['order_id']}: {status}")

channel.basic_consume(queue='order_queue', on_message_callback=process_order, auto_ack=True)
print(' [*] Ожидание сообщений из RabbitMQ. Нажми CTRL+C для выхода')
channel.start_consuming()
