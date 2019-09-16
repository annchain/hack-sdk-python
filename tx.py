from hex import from_string, to_string


class TX:

    def __init__(self, parents, nonce, sender, guarantee, pubkey, to=None, value=0):
        """
        :param parents: hex string list that contains tx parents' hashes.
        :param nonce: integer with fixed 4 bytes length, regard as int32.
        :param sender: hex string, represents the sender address.
        :param to: hex string, represents the receiver address.
        :param value: integer.
        :param pubkey: hex string.
        """
        self.parents = parents
        self.nonce = nonce
        self.sender = sender
        self.guarantee = guarantee
        self.pubkey = pubkey
        self.to = to
        self.value = value
        self.sig = b''

    def sig_target(self):

        parents_str = ""
        if len(self.parents) == 1:
            parents_str = from_string(self.parents[0])
        elif len(self.parents) == 2:
            p0 = self.parents[0]
            p1 = self.parents[1]
            if p0 <= p1:
                parents_str = from_string(p0) + from_string(p1)
            else:
                parents_str = from_string(p1) + from_string(p0)
        msg_parents = parents_str
        msg_nonce = self.nonce.to_bytes(8, byteorder='big')
        msg_from = from_string(self.sender)
        msg_to = from_string(self.to) if self.to is not None else from_string('0000000000000000000000000000000000000000')
        msg_value = self.value.to_bytes((self.value.bit_length() // 8) + 1, byteorder='big')
        msg_guarantee = self.guarantee.to_bytes((self.guarantee.bit_length() // 8) + 1, byteorder='big')

        msg = msg_parents + msg_nonce + msg_from + msg_to + msg_value + msg_guarantee
        # print(to_string(msg))
        return msg

    def sign(self, priv):
        msg = self.sig_target()
        sig = priv.sign_recoverable(msg)

        self.sig = sig
        return self.sig
