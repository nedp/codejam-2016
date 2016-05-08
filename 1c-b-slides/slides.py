#!/usr/bin/env python3

def slides(B, M):
    pass

def oracle(B, M, result):
    pass

if __name__ == '__main__':
    T = int(input())
    for i in range(1, T+1):
        B, M = map(int, input().split())

        result = slides(B, M)
        oracle(B, M, result)

        if not M:
            output = 'IMPOSSIBLE'
        else:
            output = 'POSSIBLE'
            for row in result:
                output += ''.join(row)

        print("Case #{}: {}".format(i, output))
