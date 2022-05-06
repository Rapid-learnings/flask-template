from kafka import KafkaProducer
from time import sleep
from json import dumps

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda m: dumps(m).encode('utf-8'),
    api_version=(0, 10, 1))

#if __name__ == "__main__":
for i in range(1,5):
        producer.send('youtube',value="hello Kafka, How are you!!")
        print(i)
        sleep(0.3)