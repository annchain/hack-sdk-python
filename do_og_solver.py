from account import Account, global_accounts
from hex import to_string
from og_solver import OGSolver

url = "http://172.28.152.102:38000"
private_key = "af1b6df8cc06d79902029c0e446c3dc2788893185759d2308b5bb10aa0614b7d"


def do_queryBalance():
    og = OGSolver(url)
    my_address = 'f1b4b3de579ff16888f3340f39c45f207f2cd84d'
    print(og.query_balance(my_address))


def do_queryTransaction():
    og = OGSolver(url)
    tx_hash = '0xa80f781e993539ca0b9b76696a1aab3e5b39e3290cdc85840ae3b90694a25e55'
    print(og.query_transaction(tx_hash))


def do_queryAllTipsInPool():
    og = OGSolver(url)
    poolTxs_json = og.query_all_tips_in_pool()['data']
    # {'data': {'sequencer': {'type': 1, 'hash': '0x89b84c7f5a3dadec65c733cbf230cadc9dd16d7b8f6cb49f29f7ff7692844f2e',
    #                         'parents': ['0x7a98d1a4e816e9e82caa3a9dfb9753230d574a1f6284334a816444161e083959'],
    #                         'from': '0x7349f7a6f622378d5fb0e2c16b9d4a3e5237c187', 'nonce': 238, 'treasure': '1000',
    #                         'height': 238, 'weight': 0}, 'transactions': []}, 'err': ''}

    print(poolTxs_json)


def do_sendTx():
    og = OGSolver(url)
    my_address = global_accounts[0]['address']
    account = Account(global_accounts[0]['privkey'])
    print('xxx', to_string(account.public_key))

    nonce_json = og.query_nonce(my_address)
    print(nonce_json)
    nonce = nonce_json['data']
    print('My nonce', nonce)

    poolTxs_json = og.query_all_tips_in_pool()['data']
    sequencer = poolTxs_json['sequencer']
    txs = poolTxs_json['transactions']
    guarantee = 100

    parent_hashes = [sequencer['hash']]
    # if len(txs) != 0:
    #     parent_hashes.append(txs[0]['hash'])
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
    do_queryBalance()
    do_queryTransaction()
    do_queryAllTipsInPool()
    # do_sendTx()
