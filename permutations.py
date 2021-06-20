import init_data
import operator
import copy
import utils
from functools import reduce

def _map_indexed_2d (f, A):
    res = copy.deepcopy(A)
    for x in range(len(A)):
        for y in range(len(A[x])):
            res[x][y] = f(x, y, A)
    return res

def _theta(A, w = init_data.w):
    C = lambda x: reduce(operator.xor, map(lambda y: A[x][y], range(init_data.box_size)))
    D = lambda x: C((x-1) % init_data.box_size) ^ (utils.rot(C((x+1) % init_data.box_size), 1, w))
    return _map_indexed_2d(lambda x,y,a: a[x][y] ^ D(x), A)

def _ro_pi(A, w = init_data.w):
    B = copy.deepcopy(A)
    for x in range(len(A)):
        for y in range(len(A[x])):
            B[y][(2*x + 3*y) % init_data.box_size] = utils.rot(A[x][y], init_data.r_offsets[x][y], w)
    return B

def _xi(A, w = init_data.w):
    B = _ro_pi(A, w)
    return _map_indexed_2d(
            lambda x,y,a: B[x][y] ^ ((~B[(x+1) % init_data.box_size][y]) & B[(x+2) % init_data.box_size][y]),
            A)

def _iota(A, rnd,  w = init_data.w):
    A[0][0] = A[0][0] ^ rnd
    return A

def round(A, rnd, w = init_data.w):
    return _iota(_xi(_theta(A, w), w), rnd, w)
