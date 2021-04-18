def main():
    # input
    N, M = map(int, input().split())
    ss = [input() for _ in range(N)]

    # compute
    cntss = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ss[i][j] == '#':
                cntss[i][j] += 1
            if i-1 >= 0:
                if ss[i-1][j] == '#':
                    cntss[i][j] += 1
                if j-1 >= 0:
                    if ss[i-1][j-1] == '#':
                        cntss[i][j] += 1
                if j+1 < M:
                    if ss[i-1][j+1] == '#':
                        cntss[i][j] += 1
            if i+1 < N:
                if ss[i+1][j] == '#':
                    cntss[i][j] += 1
                if j-1 >= 0:
                    if ss[i+1][j-1] == '#':
                        cntss[i][j] += 1
                if j+1 < M:
                    if ss[i+1][j+1] == '#':
                        cntss[i][j] += 1
            if j-1 >= 0:
                if ss[i][j-1] == '#':
                    cntss[i][j] += 1
            if j+1 < M:
                if ss[i][j+1] == '#':
                    cntss[i][j] += 1

    # output
    for i in range(N):
        for j in range(M-1):
            print(cntss[i][j], end='')
        print(cntss[i][M-1])


if __name__ == '__main__':
    main()
