from kafka import KafkaProducer
from time import sleep
from json import dumps

producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda m: dumps(m).encode('utf-8'),
        api_version=(0, 10, 1)
)

i=0;
while True:
    i+=1;
    print(i)
    producer.send('newtest',value=i)
