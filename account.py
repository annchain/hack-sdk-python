import coincurve

from Crypto.Hash import keccak

known_addresses = [
    'c4321fee1e29b13b042feab06dea55e7caf85948',
    'bd5ecc4dbd974ba26f6719f3207a3bd0c39c1254',
    '3cc5e3e970050256d4c0650256a1704fd2f54029',
    '147ff52dd9601f79fb86858d39384b2a9f1a1d28',
    '342f6c717be535831f10da5b2102f32c1458977f',
    'ed69714896a600bb72a0d9d9e170c1c062cedd37',
    'a98263f3022dceba151c021503a9148968be3e48',
    '88112a01269009f19562dc27c7228a8403eb135c',
    '7a4629601714224b0cf81e606b91b61f4fd852f1',
    '8198e44922faf267211627687866e5612dbd4e87',
]

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
