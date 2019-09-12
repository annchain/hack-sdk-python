from account import Account, global_accounts
from hex import to_string
from og_solver import OGSolver

url = "http://172.28.152.102:38000"
private_key = "af1b6df8cc06d79902029c0e446c3dc2788893185759d2308b5bb10aa0614b7d"

# Here is the sample code for all APIs

def do_query_nonce():
    og = OGSolver(url)
    my_address = 'f1b4b3de579ff16888f3340f39c45f207f2cd84d'
    print(og.query_nonce(my_address))
    # {'data': 3, 'err': ''}


def do_query_balance():
    og = OGSolver(url)
    my_address = 'f1b4b3de579ff16888f3340f39c45f207f2cd84d'
    print(og.query_balance(my_address))
    # {'data': {'address': 'f1b4b3de579ff16888f3340f39c45f207f2cd84d', 'balance': '1001200'}, 'err': ''}


def do_query_transaction():
    og = OGSolver(url)
    tx_hash = '0x9f672f56f950654b374ebe2330af6be9b276f511884da83a8019c4c2f70ba998'
    print(og.query_transaction(tx_hash))


def do_query_sequencer_by_hash():
    og = OGSolver(url)
    tx_hash = '0x9f672f56f950654b374ebe2330af6be9b276f511884da83a8019c4c2f70ba998'
    print(og.query_sequencer_by_hash(tx_hash))
    # {'data': {'type': 1, 'hash': '0x9f672f56f950654b374ebe2330af6be9b276f511884da83a8019c4c2f70ba998', 'parents': ['0xf973341546ba606b5329a3c532a857bb7f3cab8021f2eb803cd50013376e25af'], 'from': '0x7349f7a6f622378d5fb0e2c16b9d4a3e5237c187', 'nonce': 2, 'treasure': '1000', 'height': 2, 'weight': 2}, 'err': ''}


def do_query_sequencer_by_height():
    og = OGSolver(url)
    height = 2
    print(og.query_sequencer_by_height(height))
    # {'data': {'type': 1, 'hash': '0x9f672f56f950654b374ebe2330af6be9b276f511884da83a8019c4c2f70ba998', 'parents': ['0xf973341546ba606b5329a3c532a857bb7f3cab8021f2eb803cd50013376e25af'], 'from': '0x7349f7a6f622378d5fb0e2c16b9d4a3e5237c187', 'nonce': 2, 'treasure': '1000', 'height': 2, 'weight': 2}, 'err': ''}


def do_query_txs_by_address():
    og = OGSolver(url)
    my_address = 'f1b4b3de579ff16888f3340f39c45f207f2cd84d'
    print(og.query_txs_by_address(my_address))
    # {'data': [{'type': 0, 'hash': '0x0595edeebef2b2000af60e266b71ea2c6506b7b76578185ca718d0ab552ab7f6', 'parents': ['0x5fe495a402ae8eea2ecea8625602decbed0ff507b5b6276edb06d560f7a20ac4'], 'from': '0xf1b4b3de579ff16888f3340f39c45f207f2cd84d', 'to': '0x0000000000000000000000000000000000000000', 'nonce': 3, 'guarantee': '1', 'value': '0', 'weight': 1596}, {'type': 0, 'hash': '0x6ba2a682f3d76ea7fe55d957badc85f7b0e8c6df04bfeb5c0d2cf9d8f4e799df', 'parents': ['0xd8dcb5d1deaefef8cb06a722ef3b7e19255ab2fd7468f6d4439d819428b2bad7'], 'from': '0xf1b4b3de579ff16888f3340f39c45f207f2cd84d', 'to': '0x0000000000000000000000000000000000000000', 'nonce': 2, 'guarantee': '1', 'value': '0', 'weight': 1359}, {'type': 0, 'hash': '0xc49cd5b7fc4f3d126fccce95f8856a15e51387df771ee8eff10799cbcc1c824b', 'parents': ['0xbd23e56fee8426a4188206e0bd40b51735514f116642c0b06c94f2baf12b3d80'], 'from': '0xf1b4b3de579ff16888f3340f39c45f207f2cd84d', 'to': '0x0000000000000000000000000000000000000000', 'nonce': 1, 'guarantee': '1', 'value': '0', 'weight': 1054}], 'err': ''}


def do_query_txs_by_height():
    og = OGSolver(url)
    height = 2
    print(og.query_txs_by_height(height))


def do_query_all_tips_in_pool():
    og = OGSolver(url)
    print(og.query_all_tips_in_pool())
    # {'sequencer': {'type': 1, 'hash': '0x931c353201eb65e0522b5d5a331672957a8aeb8d20d40648ccac61edad731dc0', 'parents': ['0x64614058fd1df22c2b302a617e59e1ea40f4bb231d39893ebb0dd8e7d39d2fea'], 'from': '0x7349f7a6f622378d5fb0e2c16b9d4a3e5237c187', 'nonce': 3165, 'treasure': '1000', 'height': 3165, 'weight': 0}, 'transactions': []}


def do_query_all_txs_in_pool():
    og = OGSolver(url)
    print(og.query_all_txs_in_pool())
    # {'data': {'sequencer': {'type': 1, 'hash': '0xfd2325a06047329b7c53d303c4a0172768925eaf06560bf5a7bbea32a726a91e', 'parents': ['0xbafee5b1b3560d4ee9fdac01d483ba65ad1e519ad9ab010791185631a3eee3b7'], 'from': '0x7349f7a6f622378d5fb0e2c16b9d4a3e5237c187', 'nonce': 3174, 'treasure': '1000', 'height': 3174, 'weight': 0}, 'transactions': []}, 'err': ''}


def do_send_tx():
    og = OGSolver(url)

    # my account for signing messages
    my_address = global_accounts[0]['address']
    account = Account(global_accounts[0]['privkey'])

    # get my next nonce to be used. Nonce can only be used once
    nonce_json = og.query_nonce(my_address)
    nonce = nonce_json['data']
    print('My nonce', nonce)

    # get all txs in the pool so that I can pick up two.
    poolTxs_json = og.query_all_tips_in_pool()['data']
    sequencer = poolTxs_json['sequencer']
    txs = poolTxs_json['transactions']

    # my guarantee (bet) to be used in this tx
    guarantee = 100

    # here I just pick up sequencer's hash as my only parent.
    # You may pick up 1 ~ 2 parent(s)
    parent_hashes = [sequencer['hash']]
    # if len(txs) != 0:
    #     parent_hashes.append(txs[0]['hash'])

    # send it.
    resp = og.send_tx(account, parent_hashes, nonce, my_address, guarantee, account.public_key, None, 0)
    print(resp)


def do_send_fix_tx():
    og = OGSolver(url)

    parents = ["0x5fe495a402ae8eea2ecea8625602decbed0ff507b5b6276edb06d560f7a20ac4"]
    nonce = 3
    sender = "0xf1b4b3de579ff16888f3340f39c45f207f2cd84d"
    to = None
    value = 0
    guarantee = 1
    account = Account("af1b6df8cc06d79902029c0e446c3dc2788893185759d2308b5bb10aa0614b7d")

    resp = og.send_tx(account, parents, nonce, sender, guarantee, account.public_key, None, 0)
    print(resp)


if __name__ == '__main__':
    # do_query_nonce()
    # do_query_balance()
    # do_query_transaction()
    # do_query_sequencer_by_hash()
    # do_query_sequencer_by_height()
    # do_query_txs_by_address()
    # do_query_txs_by_height()
    # do_query_all_tips_in_pool()
    do_query_all_txs_in_pool()
    # do_sendTx()
