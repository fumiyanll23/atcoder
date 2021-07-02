def main():
    # input
    N = int(input())
    CPs = [[*map(int, input().split())] for _ in range(N)]
    Q = int(input())
    LRs = [[*map(int, input().split())] for _ in range(Q)]

    # compute
    As, Bs = [], []
    sumAs, sumBs = [0], [0]
    for C,P in CPs:
        if C == 1:
            As.append(P)
            Bs.append(0)
        else:
            As.append(0)
            Bs.append(P)
        sumAs.append(sumAs[-1] + As[-1])
        sumBs.append(sumBs[-1] + Bs[-1])
    for LR in LRs:
        L, R = LR
        print(sumAs[R]-sumAs[L-1], sumBs[R]-sumBs[L-1])

    # output


if __name__ == '__main__':
    main()
