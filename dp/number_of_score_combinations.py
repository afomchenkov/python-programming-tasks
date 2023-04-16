from functools import reduce
from collections import defaultdict
from random import randint
from sys import stdin
import os
import pdb
import cProfile

# read from file
# python main.py < test.in
# save to output
# python main.py < test.in > test.out


def readint():
    return int(stdin.readline())


def readarray(typ):
    return list(map(typ, stdin.readline().split()))


def readmatrix(n):
    M = []
    for _ in range(n):
        row = readarray(int)
        assert len(row) == n
        M.append(row)
    return M


def mult(M, v):
    n = len(M)
    return [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]


def freivalds(A, B, C):
    n = len(A)
    x = [randint(0, 1000000) for j in range(n)]
    return mult(A, mult(B, x)) == mult(C, x)


if __name__ == '__main__':
    nb_edges = int(input())
    g = defaultdict(dict)
    for _ in range(nb_edges):
        u, v, weight = input().split()
        g[u][v] = int(weight)

    print(g)
    pdb.set_trace()
