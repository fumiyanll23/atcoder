def main():
    # input
    N, M = map(int, input().split())
    pSs = [list(input().split()) for _ in range(M)]
    for i in range(M):
        pSs[i][0] = int(pSs[i][0])

    # compute
    rslts = [[0]*2 for _ in range(N)]
    ac, wa = 0, 0
    for p, S in pSs:
        p -= 1
        if S == 'AC':
            rslts[p][0] += 1
            if rslts[p][0] == 1:
                ac += 1
                wa += rslts[p][1]
        elif rslts[p][0] == 0:
            rslts[p][1] += 1

    # output
    print(ac, wa)

if __name__ == '__main__':
    main()
