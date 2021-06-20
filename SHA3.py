from permutations import round
from functools import partial
import init_data
import utils
import copy
import numpy as np

def keccak_f(A):
    for i in range(init_data.n_rounds):
        A = round(A, init_data.RC[i])
    return A

def keccak(word, c = 512, d = 256):
    r = int(1600 - c)
    P = utils.pad_word(word, r/8)
    P = utils.split_every(P, init_data.w/8)
    P = map(lambda x: utils.word_to_int(x), P)
    P = utils.split_every(P, r/init_data.w)
    P = map(partial(map, utils.little_endian), P)

    S = [[0]*5 for i in range(init_data.box_size)]
    for Pi in P:
        for x in range(init_data.box_size):
            for y in range(init_data.box_size):
                if ((x + 5*y) < (r/init_data.w)):
                    S[x][y] ^= Pi[x + 5*y]
        S = keccak_f(S)
        
    Z = utils.to_str(map(partial(map, utils.little_endian), (S.transpose().rows())))

    return utils.to_str(map(lambda x: format(x, '016x'), Z))[:d/4]

SHA3_256 = keccak
SHA3_512 = partial(keccak, c = 1024, d = 512)
SHA3_384 = partial(keccak, c = 768, d = 384)
SHA3_224 = partial(keccak, c = 448, d = 224)
