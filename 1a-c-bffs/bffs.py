#!/usr/bin/env python3

from itertools import permutations

def largest(bffs):
    # Find all the 'cores'. Pairs of kids who are mutual bffs.
    cores = set()
    inverse = {kid: set() for kid in range(len(bffs))}
    for kid in range(len(bffs)):
        inverse[bffs[kid]].add(kid)
        bff = bffs[kid]
        if bffs[bff] == kid and kid < bff:
            cores.add((kid, bff))

    total = 0
    for a, b in cores:
        total += 2
        total += deepest(bffs, inverse, a, [a, b])
        total += deepest(bffs, inverse, b, [a, b])

    for kid in range(len(bffs)):
        start = kid
        used = set()
        while kid not in used:
            used.add(kid)
            kid = bffs[kid]
        if kid == start:
            total = max(total, len(used))

    return total

def deepest(bffs, inverse, root, exclude):
    best = 0
    for child in inverse[root]:
        if child in exclude: continue
        best = max(best, 1 + deepest(bffs, inverse, child, exclude + [root]))
    return best

def oracle(bffs, result):
    # Only have limited bffs.
    assert(result <= len(bffs))

if __name__ == '__main__':
    T = int(input())
    for i in range(1, T+1):
        N = int(input())

        bffs = list(map(lambda x: int(x) - 1, input().split()))

        result = largest(bffs)
        oracle(bffs, result)

        print("Case #{}: {}".format(i, result))
