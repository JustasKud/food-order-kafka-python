import json
from kafka import KafkaConsumer, KafkaProducer
from constants import ORDER_CONFIRMED_KAFKA_TOPIC, ORDER_KAFKA_TOPIC, BOOTSTRAP_SERVERS

consumer = KafkaConsumer(
    ORDER_KAFKA_TOPIC,
    bootstrap_servers=BOOTSTRAP_SERVERS
)

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS
)

print("Transaction listening...")
while True:
    for message in consumer:
        print("\nOngoing transaction...")
        consumed_message = json.loads(message.value.decode())
        print(consumed_message)

        user_id = consumed_message["user_id"]
        total_cost = consumed_message["total_cost"]

        data = {
            "customer_id": user_id,
            "customer_email": f"{user_id}@gmail.com",
            "total_cost": total_cost
        }

        print("Successful transactions...")
        producer.send(
            ORDER_CONFIRMED_KAFKA_TOPIC,
            json.dumps(data).encode("utf-8")
        )
