from math import log2, sqrt, ceil

def prime_factorize(N: int) -> list:
    res = []
    for p in range(2, int(sqrt(N))+1):
        if N%p != 0:
            continue
        ex = 0
        while N%p == 0:
            ex += 1
            N //= p
        res.append([p, ex])
    if N != 1:
        res.append([N, 1])

    return res


def main():
    # input
    N = int(input())

    # compute

    # output
    print(ceil(log2(sum([ex for p, ex in prime_factorize(N)]))))


if __name__ == '__main__':
    main()
