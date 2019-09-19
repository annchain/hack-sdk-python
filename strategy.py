import json
import traceback

from kafka import KafkaConsumer

# modify according to the specific
from account import Account
from og_solver import OGSolver

KAFKA_TOPIC = 'hack-final-test'
KAFKA_SERVER = ['47.100.222.11:30000']
API_URL = "http://172.28.152.102:30020"

private_key = "567d6a1f2d5bafae059308d91cb8a5452cb48032bed42a9ff5a601a7bab5e183"
TOKEN = '98765467890'

og = OGSolver(API_URL, TOKEN)
my_account = Account(private_key)


def on_new_tx(tx):
    if tx['type'] == 0:
        print('Received Tx: ', tx)
    elif tx['type'] == 1:
        print('Received Seq: ', tx)
        # this is the very naive policy
        # just follow the sequencer once a sequencer is generated.
        resp = og.query_nonce(my_account.address)
        nonce = resp['data']
        og.send_tx(my_account, [tx['data']['hash']], nonce + 1, my_account.address, 100, my_account.public_key)


if __name__ == '__main__':
    # this is the callback for receiving a new tx:
    consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_SERVER)
    for message in consumer:
        tx = json.loads(message.value.decode('utf-8'))
        try:
            on_new_tx(tx)
        except:
            traceback.print_exc()
