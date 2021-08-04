def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]
    MOD = 10**9 + 7

    # compute
    As = sorted([*set(As)])
    As.insert(0, 0)
    ans = 1
    for ai, aj in zip(As, As[1:]):
        ans = ans * (aj - ai + 1) % MOD

    # output
    print(ans)


if __name__ == '__main__':
    main()
