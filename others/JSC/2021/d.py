def main():
    # input
    N, P = map(int, input().split())
    MOD = 10**9 + 7

    # compute

    # output
    print(((P-1)*pow((P-2), (N-1), MOD)) % MOD)


if __name__ == '__main__':
    main()
