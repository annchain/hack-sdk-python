import json

from kafka import KafkaConsumer

# modify according to the specific
from account import Account
from og_solver import OGSolver

KAFKA_TOPIC = 'hack-final-test'
KAFKA_SERVER = ['47.100.222.11:30000']
API_URL = "http://172.28.152.102:38000"

private_key = "af1b6df8cc06d79902029c0e446c3dc2788893185759d2308b5bb10aa0614b7d"
TOKEN = '98765467890'

og = OGSolver(API_URL, TOKEN)
my_account = Account(private_key)

KAFKA_TOPIC = 'hack-final-test'
KAFKA_SERVER = ['47.100.222.11:30000']
API_URL = "http://172.28.152.102:38000"


def on_new_tx(tx):
    if tx['type'] == 0:
        print('Received Tx: ', tx)
        # j = og.query_balance(my_account.address)
        # print(j)

    elif tx['type'] == 1:
        print('Received Seq: ', tx)
        # j = og.query_txs_by_height(tx['data']['height'])
        # print('txs', j)
        # j = og.query_sequencer_by_height(tx['data']['height'])
        # # {'type': 1, 'data': {'type': 1, 'hash': '0x2c4f87904d2ba37512511506a102b638bfcff8534b652dd288c498372b4bb6ee', 'parents': ['0xda2ea8f640300ffe8ae27ee7ce63ca012e24fb06ce170089dfaeb952cdb21c70'], 'from': '0x7349f7a6f622378d5fb0e2c16b9d4a3e5237c187', 'nonce': 65754, 'treasure': '1000', 'height': 65754, 'weight': 65757}}
        # print('seq', j)


if __name__ == '__main__':
    # load accounts


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
