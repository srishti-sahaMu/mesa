from kafka import KafkaConsumer
#connect to Kafka server and pass the topic we want to consume
consumer = KafkaConsumer('testtopic1', group_id='view', bootstrap_servers=['0.0.0.0:9092'])

def kafkastream():
    for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))    

