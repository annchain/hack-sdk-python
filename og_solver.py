import numpy as np
import account
import requests

from tx import TX
from account import Account


# import secp256k1


class OGSolver:

    def __init__(self, url):
        """
        :param url: hex string. e.g. 127.0.0.1:10003
        """
        self.url = url

    def send_tx(self, account, parents, nonce, sender, guarantee, pubkey, to=None, value=0):
        # TODO
        #  check the inputs

        tx = TX(parents, nonce, sender, guarantee, pubkey, to, value)
        tx.sig = tx.sign(account.private_key)

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

        print(data)
        url = self.url + "/new_transaction"
        r = requests.post(url, json=data)
        print(r.text)
        return r.json()

    def query_nonce(self, address):
        # TODO
        #  check the input

        params = {
            "address": address
        }
        url = self.url + "/query_nonce"
        r = requests.get(url=url, params=params)

        return r.json()

    def query_balance(self, address):
        # TODO
        #  check the input

        params = {
            "address": address
        }
        url = self.url + "/query_balance"
        r = requests.get(url=url, params=params)

        return r.json()

    def query_pool(self):
        """
        get all the txs that currently in the pool
        :return:
        """

        # TODO
        #  check the input
        pass

    def query_transaction(self, tx_hash):
        params = {
            "hash": tx_hash
        }
        url = self.url + "/transaction"
        r = requests.get(url=url, params=params)

        return r.json()

    def query_all_tips_in_pool(self):
        url = self.url + "/query_pool_tips"
        r = requests.get(url=url)

        return r.json()