def from_string(hex_string: str):
    if hex_string.startswith('0x'):
        hex_string = hex_string[2:]
    return bytearray.fromhex(hex_string)


def to_string(bytearray, prefix=True):
    s = ''.join('{:02x}'.format(x) for x in bytearray)
    if prefix:
        s = '0x' + s
    return s
