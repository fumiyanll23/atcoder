def main():
    # input
    N = int(input())
    Cs = [*map(int, input().split())]
    MOD = 10**9 + 7

    # compute
    ans = 1
    Cs.sort()
    for i, C in enumerate(Cs):
        ans = (ans * (C-i)) % MOD
        if ans <= 0:
            print(0)
            exit()

    # output
    print(ans)


if __name__ == '__main__':
    main()
