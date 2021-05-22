def main():
    # input
    A, B, K = map(int, input().split())

    # compute
    dp = [[0]*B for _ in range(A)]

    ## define function find_kth
    def find_kth(A: int, B: int, K: int) -> str:
        if A == 0:
            return 'b' * B
        elif B == 0:
            return 'a' * A
        elif K <= dp[A-1][B]:
            return 'a' + find_kth(A-1, B, K)
        else:
            return 'b' + find_kth(A, B-1, K-dp[A-1][B])

    dp[0][0] = 1
    for i in range(A):
        for j in range(B):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            elif j > 0:
                dp[i][j] += dp[i][j-1]

    # output
    print(find_kth(A, B, K))


if __name__ == '__main__':
    main()
