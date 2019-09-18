import requests

from hex import to_string
from tx import TX


class OGSolver:

    def __init__(self, url, token):
        """
        :param url: hex string. e.g. 127.0.0.1:10003
        """
        self.url = url
        self.token = token

    def send_tx(self, account, parents, nonce, sender, guarantee, pubkey, to=None, value=0):
        # TODO
        #  check the inputs

        tx = TX(parents, nonce, sender, guarantee, pubkey, to, value)
        print(tx.dump())
        tx.sig = tx.sign(account.private_key)
        print("sig", to_string(tx.sig))

        data = {
            "parents": tx.parents,
            "from": tx.sender,
            "to": tx.to,
            "nonce": tx.nonce,
            "guarantee": str(tx.guarantee),
            "value": str(tx.value),
            "signature": tx.sig.hex(),
            "pubkey": tx.pubkey.hex(),
        }

        # print(data)
        url = self.url + "/new_transaction"
        r = requests.post(url, json=data, headers={'cookie': 'token=' + self.token})
        print("TEXT", r.text)
        return r.json()

    def query_nonce(self, address):
        # TODO
        #  check the input

        params = {
            "address": address
        }
        url = self.url + "/query_nonce"
        r = requests.get(url=url, params=params, headers={'cookie': 'token=' + self.token})

        return r.json()

    def query_balance(self, address):
        # TODO
        #  check the input

        params = {
            "address": address
        }
        url = self.url + "/query_balance"
        r = requests.get(url=url, params=params, headers={'cookie': 'token=' + self.token})

        return r.json()

    def query_transaction(self, tx_hash: str):
        params = {
            "hash": tx_hash
        }
        url = self.url + "/transaction"
        r = requests.get(url=url, params=params, headers={'cookie': 'token=' + self.token})

        return r.json()

    def query_sequencer_by_hash(self, seq_hash: str):
        params = {
            "hash": seq_hash
        }
        url = self.url + "/sequencer"
        r = requests.get(url=url, params=params, headers={'cookie': 'token=' + self.token})
        return r.json()

    def query_sequencer_by_height(self, height: int):
        params = {
            "height": height
        }
        url = self.url + "/sequencer"
        r = requests.get(url=url, params=params, headers={'cookie': 'token=' + self.token})
        return r.json()

    def query_txs_by_address(self, address: str):
        params = {
            "address": address
        }
        url = self.url + "/transactions"
        r = requests.get(url=url, params=params, headers={'cookie': 'token=' + self.token})
        return r.json()

    def query_txs_by_height(self, height: int):
        params = {
            "height": height
        }
        url = self.url + "/transactions"
        r = requests.get(url=url, params=params, headers={'cookie': 'token=' + self.token})
        return r.json()

    def query_all_tips_in_pool(self):
        url = self.url + "/query_pool_tips"
        r = requests.get(url=url, headers={'cookie': 'token=' + self.token})
        return r.json()

    def query_all_txs_in_pool(self):
        url = self.url + "/query_pool_txs"
        r = requests.get(url=url, headers={'cookie': 'token=' + self.token})

        return r.json()
