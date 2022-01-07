import sys
import re
from collections import defaultdict
import random as rnd


def get_tokenized_text(f):
    p = re.compile(r"\S+|\n    ")
    text = f.read()
    return p.findall(text)


def form_dict(toks):
    d = defaultdict(set)
    for tok1, tok2, tok3 in zip(toks, toks[1:], toks[2:]):
        d[(tok1, tok2)].add(tok3)
    d = dict(d)
    return d


if __name__ == "__main__":
    N = int(input())
    tokenized_text = get_tokenized_text(sys.stdin)
    d = form_dict(tokenized_text)

    start = rnd.choice(list(d))
    start_tok3 = rnd.choice(list(d[start]))
    last_two = (start[1], start_tok3)

    print(*start, start_tok3, end=" ")

    N -= 3

    while N > 0:
        next_tok = rnd.choice(list(d[last_two]))
        last_two = (last_two[1], next_tok)

        print(next_tok, end=" ")
        N -= 1
