import json
import random

from kafka import KafkaConsumer

from account import Account
from hex import to_string
from og_solver import OGSolver

global_accounts = [
    '567d6a1f2d5bafae059308d91cb8a5452cb48032bed42a9ff5a601a7bab5e183',  # c4321fee1e29b13b042feab06dea55e7caf85948
    'd9fcf0b7789ebc007ab87acddaad50687973f9c065b1f1e0d43330d6d150fbc3',  # bd5ecc4dbd974ba26f6719f3207a3bd0c39c1254
    'c37421b012240d8f320eacf5d9bd378409ecbf8536b9bdeb85f45e94dd106c22',  # 3cc5e3e970050256d4c0650256a1704fd2f54029
    '92d12f7ff94ccecf1f5f61fc0b26b429ba9405bf1acb9ced1c3e9168d9cf6c81', # 147ff52dd9601f79fb86858d39384b2a9f1a1d28
    # 'ddda818cde6a873dd6cf4967ea9de63d87f36419bc1798bb5197ddb8c6cf6663',
    # '7dd6f2cf395532f4ede10b7c365f035d89a152926ee7209877299a3a24b6eb41',
    # '5b659920b75435d91c35ce9c171ea7117218c08585bde2497922437da0bc2e13',  # a98263f3022dceba151c021503a9148968be3e48
    # 'c428f0c23547cae15a8c8c0e9f1987c96a9f13259884e93a72868b9833abb3be',
    # 'e5e681a49c1b3e7f4aa016ee45dc2a8bbc55f03aa666120e7967f5dd7498bd94',
    # 'd4a8ad200e3fa4d181c9f9c1651e15180aa31103458e86c57adff7d6dbf7528a',
]

KAFKA_TOPIC = 'hack-final-test'
KAFKA_SERVER = ['47.100.222.11:30000']
# API_URL = "http://172.28.152.102:38000"
API_URL = "http://172.28.152.102:30020"
TOKEN = '98765467890'

account_map = {}
accounts = []
og_solver = OGSolver(API_URL, TOKEN)

strategy = {
    -1: [(0, 1)],
    0: [],
    1: [],
    2: [],
    # 2: [(3, 50)],
    # 3: [],
}

# generate accounts
if __name__ == '__main__1':
    # generate accounts
    print('private public address')
    for i in range(10):
        bits = random.getrandbits(256)
        # 30848827712021293731208415302456569301499384654877289245795786476741155372082
        bits_hex = hex(bits)
        # 0x4433d156e8c53bf5b50af07aa95a29436f29a94e0ccc5d58df8e57bdc8583c32
        private_key = bits_hex[2:]
        account = Account(private_key)
        print(account.private_key.to_hex(), to_string(account.public_key)[2:], account.address)


def check_nonce(account_me):
    # if account_me.nonce == 0:
    account_me.nonce = og_solver.query_nonce(account_me.address)['data'] + 1


def on_new_tx(tx):
    if tx['type'] == 0:
        print('Received Tx: ', tx)
        # detect the sender
        sender_index = account_map[tx['data']['from'][2:]]
        # fetch all nodes interested in tx
        for acc_index, bet in strategy[sender_index]:
            account_me = accounts[acc_index]
            check_nonce(account_me)
            og_solver.send_tx(account_me, [tx['data']['hash']], account_me.nonce, account_me.address, bet,
                              account_me.public_key)
    elif tx['type'] == 1:
        print('Received Seq: ', tx)
        # fetch all nodes interested in seq
        for acc_index, bet in strategy[-1]:
            account_me = accounts[acc_index]
            check_nonce(account_me)
            og_solver.send_tx(account_me, [tx['data']['hash']], account_me.nonce, account_me.address, bet,
                              account_me.public_key)


# {'type': 1, 'data': {'type': 1, 'hash': '0x2c4f87904d2ba37512511506a102b638bfcff8534b652dd288c498372b4bb6ee',
# 'parents': ['0xda2ea8f640300ffe8ae27ee7ce63ca012e24fb06ce170089dfaeb952cdb21c70'], 'from': '0x7349f7a6f622378d5fb0e2c16b9d4a3e5237c187',
# 'nonce': 65754, 'treasure': '1000', 'height': 65754, 'weight': 65757}}


# sample strategy
if __name__ == '__main__':
    i = 0
    for priv in global_accounts:
        a = Account(priv)
        accounts.append(a)
        account_map[a.address] = i
        i += 1

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
