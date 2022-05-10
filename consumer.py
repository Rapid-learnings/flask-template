from kafka import KafkaConsumer

consumer = KafkaConsumer(
                'youtube',
                bootstrap_servers=['localhost:9092'],
                auto_offset_reset = 'latest',  
                enable_auto_commit=True,
                auto_commit_interval_ms=100,
                group_id="test-consumer-group",
                api_version=(0, 10, 1)
        )

for message in consumer:
    print(message.value)


