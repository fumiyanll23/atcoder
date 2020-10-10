def main():
    n, k = map(int, input().split())
    V = [[0]*(n+1)] + [[0] + sorted(list(map(int, input().split())))
                       for _ in range(n)]
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for ni in range(1, n):
        val = 0
        ki = 1
        for kj in range(1, k+1):
            while ki <= k and V[ni+1][kj] >= V[ni][ki]:
                if ni == 1:
                    val = ki
                else:
                    val += dp[ni][ki]
                ki += 1
            dp[ni+1][kj] = val
    print(sum(dp[n]) % (10**9 + 7))
if __name__ == '__main__':
    main()
