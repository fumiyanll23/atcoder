def binary_search(xs: list, key: int) -> int:
    ng, ok = -1, len(xs)
    while ok-ng > 1:
        middle = ng + (ok-ng)//2
        if xs[middle] >= key:
            ok = middle
        else:
            ng = middle

    return ok


def main():
    # input
    N, Q = map(int, input().split())
    As = [*map(int, input().split())]
    Ks = [int(input()) for _ in range(Q)]

    # compute
    cnts = [0] * N
    for i,A in enumerate(As):
        cnts[i] = A - (i+1)

    # output
    for K in Ks:
        idx = binary_search(cnts, K) - cnts[0]
        if idx == N:
            print(As[-1] + (K - cnts[-1]))
        else:
            print(As[idx] - (cnts[idx]-K+1))


if __name__ == '__main__':
    main()
