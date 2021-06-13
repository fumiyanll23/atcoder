def binary_search(xs: list, key: int) -> int:
    ng, ok = -1, len(xs)
    while ok-ng > 1:
        middle = ng + (ok-ng)//2
        if xs[middle] > key:
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

    # output
    for K in Ks:
        flag = binary_search(As, K)
        if K < As[0]:
            print(K)
        elif K >= As[-1]:
            print(K + N)
        else:
            print('flag', flag, K+flag)


if __name__ == '__main__':
    main()
