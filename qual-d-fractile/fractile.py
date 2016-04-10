#!/usr/bin/env python3

IMPOSSIBLE = 'IMPOSSIBLE'

def tiles(K, C, S):
    if K <= S:
        return list(range(1, K + 1))

    all_digits = range(K)

    # Split the original tiles into evenly sized chunks.
    # Round up to ensure we cover all original tiles.
    width = (K + S - 1) // S

    # If there's not enough information per chunk, give up.
    if width > C:
        return IMPOSSIBLE

    result = []

    # For each student:
    for i in range(S):
        # Have each student verify their allocated tiles from the
        # original pattern; one chunk per student.
        my_digits = all_digits[width * i: min(width * (i+1), K)]

        # If we already have all the information, break.
        if not my_digits:
            break

        # Interpret my assigned original tiles as a base-K number,
        # which will tell me my actual tile.
        my_tile = from_base(my_digits, K)

        assert(my_tile < K**C)

        result.append(my_tile + 1)

    return result


def oracle(K, C, S, result):
    if result == IMPOSSIBLE:
        assert(C*S < K)
        return

    # We only have S students.
    assert(len(result) <= S)

    # There should be no duplicates
    sorted_result = sorted(result)
    for p, c in zip(sorted_result[:-1], sorted_result[1:]):
        assert(c != p)

    # Make sure the chosen tiles actually exist.
    max_tile = K**C
    for tile in result:
        assert(0 < tile <= max_tile)

    # Simulate cleaning the tiles and constructing knowledge set.
    unknown = set(range(K))
    for tile in result:
        revealed_tiles = to_base(tile - 1, K, C)
        for i in revealed_tiles:
            if i in unknown:
                unknown.remove(i)
    assert(not unknown)

def to_base(n, base, width):
    if width is None:
        width = base
    result = []

    for _ in range(width):
        digit = n % base
        result.append(digit)

        n -= digit
        assert(n % base == 0)
        n = n // base

    return result

def from_base(digits, base):
    offset = 1
    result = 0
    for d in digits:
        result += offset * d
        offset *= base

    for a, b in zip(to_base(result, base, len(digits)), digits):
        assert(a == b)

    return result

if __name__ == '__main__':

    T = int(input())
    for i in range(1, T+1):
        K, C, S = map(int, input().split(' '))
        result = tiles(K, C, S)
        oracle(K, C, S, result)

        items = map(str, result) if result != IMPOSSIBLE else [IMPOSSIBLE]

        print("Case #{}: {}".format(i, ' '.join(items)))

