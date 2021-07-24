def main():
    # input
    S = input()
    MOD = 10**9 + 7

    # compute
    N = len(S)
    T = '0chokudai'
    M = len(T)
    dp = [[0]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = 0
            else:
                if S[i] != T[j]:
                    dp[i][j] = dp[i-1][j] % MOD
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % MOD

    # output
    print(dp[-1][-1])


if __name__ == '__main__':
    main()
