def main():
    # input
    N, Q = map(int, input().split())
    Sss = [list(map(int, input().split())) for _ in range(Q)]

    # compute
    ansss = [['N']*N for _ in range(N)]
    for i in range(Q):
        if Sss[i][0] == 1:
            ansss[Sss[i][1]-1][Sss[i][2]-1] = 'Y'
        elif Sss[i][0] == 2:
            for j in range(N):
                if ansss[j][Sss[i][1]-1] == 'Y':
                    ansss[Sss[i][1]-1][j] = 'Y'
        elif Sss[i][0] == 3:
            for j in range(N):
                if ansss[Sss[i][1]-1][j] == 'Y':
                    print(Sss[i][1]-1, j)
                    for k in range(N):
                        if ansss[j][k] == 'Y':
                            print(Sss[i][1]-1, j, k)
                            ansss[Sss[i][1]-1][k] = 'Y'

    # output
    for i in range(N):
        print(ansss[i])


if __name__ == '__main__':
    main()
