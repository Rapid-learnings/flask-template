from kafka import KafkaConsumer
from json import loads

def consumer_fub():
        consumer = KafkaConsumer(
                        'newtest',
                        bootstrap_servers=['localhost:9092'],
                        auto_offset_reset = 'latest',
                        max_poll_interval_ms=2000,
                        max_poll_records=1,  
                        enable_auto_commit=True,
                        group_id=None,
                        consumer_timeout_ms=1000,
                        value_deserializer=lambda m: loads(m.decode('utf-8')),
                        api_version=(0, 10, 1)
        )
        
        for message in consumer:
                #message = message.poll()
                message = message.value;
                print(f" Printing Random Number {'{}'.format(message)}")
        consumer.close()
                
