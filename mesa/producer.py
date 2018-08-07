# producer.py

from kafka import SimpleProducer, KafkaClient, KafkaProducer
#  connect to Kafka
kafka = KafkaClient('localhost:9092')
producer = KafkaProducer(kafka)
# Assign a topic
topic = 'testtopic1'

def msg_emitter(df):
    
    print(' emitting.....')
    # Convert the test string to bytes and send to kafka
    df_bytes = df.encode()
    producer.send(topic, df_bytes)
    producer.flush()
    print('done emitting')

