def main():
    # input
    N = int(input())
    Ts = [*map(int, input().split())]
    M = int(input())
    PXs = [[*map(int, input().split())] for _ in range(M)]

    # compute
    Tsum = sum(Ts)

    # output
    for P, X in PXs:
        print(Tsum - Ts[P-1] + X)


if __name__ == '__main__':
    main()
