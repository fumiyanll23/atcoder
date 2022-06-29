def main():
    # input
    N = int(input())
    Ts = [*map(int, input().split())]
    M = int(input())
    PXs = [[*map(int, input().split())] for _ in range(M)]

    # compute

    # output
    for P, X in PXs:
        tmp_Ts = list(Ts)
        tmp_Ts[P-1] = X
        print(sum(tmp_Ts))


if __name__ == '__main__':
    main()
