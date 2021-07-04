def main():
    # input
    N, M = map(int, input().split())
    ABCss = [[*map(int, input().split())] for _ in range(M)]

    # compute
    INF = 10**6 + 1
    ans = 0
    dp = [[INF]*N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
    for ABCs in ABCss:
        A, B, C = ABCs
        dp[A-1][B-1] = C
    for K in range(N):
        for k in range(N):
            if k > K:
                continue
            for i in range(N):
                for j in range(N):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
                    if dp[i][j] != INF:
                        ans += dp[i][j]

    # output
    print(ans // 2)


if __name__ == '__main__':
    main()
