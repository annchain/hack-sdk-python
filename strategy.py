import json

from kafka import KafkaConsumer

# modify according to the specific
KAFKA_TOPIC = 'hack-final-test'
KAFKA_SERVER = ['47.100.222.11:30000']


def on_new_tx(tx):
    if tx['type'] == 0:
        print('Received Tx: ', tx)
    elif tx['type'] == 1:
        print('Received Seq: ', tx)


if __name__ == '__main__':
    # this is the callback for receiving a new tx:
    consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_SERVER)
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        # print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
        #                                      message.offset, message.key,
        #                                      message.value))

        tx = json.loads(message.value.decode('utf-8'))
        on_new_tx(tx)
