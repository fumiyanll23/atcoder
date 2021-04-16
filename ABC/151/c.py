def main():
    # input
    N, M = map(int, input().split())
    pSs = [list(input().split()) for _ in range(M)]
    for i in range(M):
        pSs[i][0] = int(pSs[i][0])

    # compute
    rslts = [[0]*2 for _ in range(N)]
    ac, wa = 0, 0
    for i in range(M):
        if pSs[i][1] == 'AC':
            rslts[pSs[i][0]-1][0] += 1
            if rslts[pSs[i][0]-1][0] == 1:
                ac += 1
        elif rslts[pSs[i][0]-1][0] == 0:
            rslts[pSs[i][0]-1][1] += 1
            wa += 1
    for i in range(N):
        if rslts[i][0] == 0:
            wa -= rslts[i][1]

    # output
    print(ac, wa)

if __name__ == '__main__':
    main()
