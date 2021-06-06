def main():
    # input
    N, M = map(int, input().split())
    ABs = [[*map(int, input().split())] for _ in range(M)]

    # compute
    Ess = [[0]*N for _ in range(N)]
    for AB in ABs:
        a, b = AB
        Ess[a-1][b-1] = 1
    for i in range(N):
        Ess[i][i] = 1

    # output
    print(Ess)
    print(sum([sum(Es) for Es in Ess]))


if __name__ == '__main__':
    main()
