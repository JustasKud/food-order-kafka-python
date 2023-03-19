import json
from kafka import KafkaConsumer
from constants import ORDER_CONFIRMED_KAFKA_TOPIC, BOOTSTRAP_SERVERS

consumer = KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC,
    bootstrap_servers=BOOTSTRAP_SERVERS
)

emails_sent_so_far = set()
print("Emails listening...")
while True:
    for message in consumer:
        consumed_message = json.loads(message.value.decode())
        customer_email = consumed_message["customer_email"]
        print(f"\nSending email to {customer_email}")
        emails_sent_so_far.add(customer_email)
        print(f"So far emails sent to {len(emails_sent_so_far)} unique emails")
