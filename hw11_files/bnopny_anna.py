from itertools import product
import sys
from collections import deque
from typing import final

possible_encodings = ["cp1026", "cp1140", "cp1256", "cp273", "cp437", "cp500", "cp775", "cp850", "cp852", "cp855", "cp857", "cp860", "cp861", "cp862", "cp863", "cp865", "cp866", "gb18030", "hp_roman8",
                      "iso8859_10", "iso8859_11", "iso8859_13", "iso8859_14", "iso8859_15", "iso8859_16", "iso8859_2", "iso8859_4", "iso8859_5", "iso8859_9", "koi8_r", "mac_cyrillic", "mac_greek", "mac_latin2", "mac_roman", "utf_8"]

def encode_with_chain(data, chain):
    enc = data
    for e1, e2 in chain:
        enc = enc.decode(e1).encode(e2)
    return enc

def decode_with_chain(data, chain):
    dec = data
    for e1, e2 in reversed(chain):
        dec = dec.decode(e2).encode(e1)
    return dec

invariant = ", что"
invariant_bytes = invariant.encode()

def main():
    encoded = sys.stdin.buffer.read()
    # encoded = open("bnopnya1.bin", 'rb').read()

    possible_pairs = set()

    for e1, e2 in product(possible_encodings, repeat=2):
        if e1 == e2 or (e2, e1) in possible_pairs:
            continue
        
        try: 
            invariant_reenc = invariant_bytes.decode(e1).encode(e2)
            invariant2 = invariant_reenc.decode(e2).encode(e1)
        except:
            continue

        if invariant2 == invariant_bytes:
            possible_pairs.add((e1, e2))

            if invariant_reenc in encoded:
                decoded = encoded.decode(e2).encode(e1)

                if invariant_bytes in decoded:
                    print(decoded.decode().splitlines()[0])
                    return

    possible_chains = set()

    for chain in product(possible_pairs, repeat=2):
        try:
            enc = encode_with_chain(invariant_bytes, chain)
            res = decode_with_chain(enc, chain)
        except:
            continue

        if invariant_bytes == res:
            possible_chains.add(chain)

            if enc in encoded:
                decoded_bnopnya = decode_with_chain(encoded, chain)

                if invariant_bytes in decoded_bnopnya:
                    print(decoded_bnopnya.decode().splitlines()[0])
                    return
    
    for chain, p in product(possible_chains, possible_pairs): 
        chain = (*chain, p)
        try:
            enc = encode_with_chain(invariant_bytes, chain)
            res = decode_with_chain(enc, chain)
        except:
            continue
        
        if invariant_bytes == res and enc in encoded:
            decoded_bnopnya = decode_with_chain(encoded, chain)
            if invariant_bytes in decoded_bnopnya:
                print(decoded_bnopnya.decode().splitlines()[0])
                return


if __name__ == "__main__":
    main()