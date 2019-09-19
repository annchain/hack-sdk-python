import coincurve

from Crypto.Hash import keccak


class Account:
    def __init__(self, priv):
        """
        :param priv: hex
        """

        private_key = coincurve.PrivateKey(bytearray.fromhex(priv))
        public_key = private_key.public_key

        self.nonce = 0
        self.private_key = private_key
        self.public_key = public_key.format(compressed=False)

        keccak_hash = keccak.new(digest_bits=256)
        keccak_hash.update(self.public_key[1:])

        self.address = keccak_hash.hexdigest()[-40:]
