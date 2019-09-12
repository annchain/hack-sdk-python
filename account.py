import coincurve

global_accounts = [
    {'privkey': 'af1b6df8cc06d79902029c0e446c3dc2788893185759d2308b5bb10aa0614b7d',
     'address': 'f1b4b3de579ff16888f3340f39c45f207f2cd84d'},
    {'privkey': '1f9b9a2696254107fce41332f83970d7f040bf71bd52e16ff2a06d9255be9de9',
     'address': '4d08ef9a51793c15bea11ad55e5c3fae602745ee'},
    {'privkey': '33b566d349aa3351692655fb385074c0f7275a814a2deeafd16195723dd212fd',
     'address': '8601b8d851d4efc019d690a772ee75235ee8a84f'},
    {'privkey': 'ea5c638caa5c216823b87bf7bc034d50db69afdf1a852024e12fd83b83befafe',
     'address': '7b07149eab34c40b5cc2d8b995a7c60922f3485a'},
    # {'privkey': '40fbc53fbd2771662bbf21d2d145dcf87d90328022bc33f4270d1aa61aee8e27',
    # 'address': 'a04ba065b6b99d105a9d2c76cf10fa01271e4e8b'},
    # {'privkey': '40fbc53fbd2771662bbf21d2d145dcf87d90328022bc33f4270d1aa61aee8e27',
    # 'address': 'a04ba065b6b99d105a9d2c76cf10fa01271e4e8b'},
    # {'privkey': '40fbc53fbd2771662bbf21d2d145dcf87d90328022bc33f4270d1aa61aee8e27',
    # 'address': 'a04ba065b6b99d105a9d2c76cf10fa01271e4e8b'},
    # {'privkey': '40fbc53fbd2771662bbf21d2d145dcf87d90328022bc33f4270d1aa61aee8e27',
    # 'address': 'a04ba065b6b99d105a9d2c76cf10fa01271e4e8b'},
    # {'privkey': '40fbc53fbd2771662bbf21d2d145dcf87d90328022bc33f4270d1aa61aee8e27',
    # 'address': 'a04ba065b6b99d105a9d2c76cf10fa01271e4e8b'},
    # {'privkey': '40fbc53fbd2771662bbf21d2d145dcf87d90328022bc33f4270d1aa61aee8e27',
    # 'address': 'a04ba065b6b99d105a9d2c76cf10fa01271e4e8b'},
]


# ----------------
# ea5c638caa5c216823b87bf7bc034d50db69afdf1a852024e12fd83b83befafe
# 7b07149eab34c40b5cc2d8b995a7c60922f3485a
# ----------------
# 38ddf9f557094607b00beabcf504166a72fa1dd658fe3929887ebd28d34c04aa
# f5b688e5330fdf85ad644b0704408a4ceda8a72b
# ----------------
# c21cdc18d09d862b9c755f3bca7e7bf045d2c4a741fd740d9f18d31aa0ab443d
# db39a92560097ef5f991134148e2fe0c52e56141
# ----------------
# 46dd04a050647f4b1d51b88a2b8354ae280f79561b4c3bbf28974c81fb59fad2
# 9363e26eb4f6d6f140fbc1d066bb0cbaac672114
# ----------------
# a5468e2a4f32c54a47690859847fa953d7c05f29fe09ff8af876ed0664c482c0
# 3fd6f6f388f2f9f8d8bfcaea9274e680f80616cc
# ----------------
# 85710306c6bf439eb3527d4ba991000055dad3e2a1cc875724de2ba299b0e38e
# b551a012ed154194686bf86a77e0a5646138496b
# ----------------
# b5ce5215afbcc2c09751a1341c71e1631b4b135e9d9e743c3c30821134ec3324
# 102f056b26cd9928facc49e719551c47a2d79b8b


class Account:
    def __init__(self, priv):
        """
        :param priv: hex
        """

        private_key = coincurve.PrivateKey(bytearray.fromhex(priv))
        public_key = private_key.public_key

        self.private_key = private_key
        self.public_key = public_key.format(compressed=False)