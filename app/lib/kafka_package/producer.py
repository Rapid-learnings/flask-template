from kafka import KafkaProducer
from time import sleep
from json import dumps
from random import randint

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda m: dumps(m).encode('utf-8'),
    api_version=(0, 10, 1)
)

while True:
    newval=f'Hello {randint(1,1000)}'
    producer.send('youtube',value=newval)
    print(newval)
    sleep(1)
