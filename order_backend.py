import json
from kafka import KafkaProducer
from constants import ORDER_LIMIT, ORDER_KAFKA_TOPIC, BOOTSTRAP_SERVERS

producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)

for i in range(1, ORDER_LIMIT + 1):
    data = {
        "order_id": i,
        "user_id": f"tom_{i}",
        "total_cost": i * 2,
        "items": "burger, sandwich"
    }

    producer.send(
        ORDER_KAFKA_TOPIC,
        json.dumps(data).encode("utf-8")
    )
    print(f"Done sending...{i}")
