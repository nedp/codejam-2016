#!/usr/bin/env python3

from math import log

def evac(P):
    pass

def oracle(P, result):
    pass

if __name__ == '__main__':
    T = int(input())
    for i in range(1, T+1):
        N = int(input())
        P = list(map(int, input().split()))
        assert(len(P) == N)

        result = evac(P)
        oracle(P, result)

        print("Case #{}: {}".format(i, result))
