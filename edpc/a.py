# input
N = int(input())
hs = [*map(int, input().split())]

# compute
dp = [1 << 30] * (N + 10)
dp[0] = 0
for i in range(N):
    dp[i] = min(dp[i], dp[i-1] + abs(hs[i] - hs[i-1]))
    if i > 1:
        dp[i] = min(dp[i], dp[i-2] + abs(hs[i] - hs[i-2]))

# output
print(dp[N-1])
