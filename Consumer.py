from kafka import KafkaConsumer
from json import loads
# from pymongo import MongoClient  

consumer = KafkaConsumer(
    'youtube',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset = 'earliest',  
    enable_auto_commit=True,
    group_id="test-consumer-group",
    #value_deserializer = lambda x : loads(x.decode('utf-8')),
    api_version=(0, 10, 1)
    )

# my_client = MongoClient('localhost : 27017')  
# my_collection = my_client.testnum.testnum  

ms=""
for message in consumer:
   ms+=str(message.value)
   print(ms)
#    collection.insert_one(message)  
#    print(message + " added to " + my_collection)
def got_fun():     
    return ms
