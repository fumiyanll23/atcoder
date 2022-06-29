def main():
    # input
    S = input()
    MOD = 10**9 + 7

    # compute
    c, h, o, k, u, d, a, ans = 0, 0, 0, 0, 0, 0, 0, 0
    for s in S:
        if s == 'c':
            c = (c + 1) % MOD
        elif s == 'h':
            h = (h + c) % MOD
        elif s == 'o':
            o = (o + h) % MOD
        elif s == 'k':
            k = (k + o) % MOD
        elif s == 'u':
            u = (u + k) % MOD
        elif s == 'd':
            d = (d + u) % MOD
        elif s == 'a':
            a = (a + d) % MOD
        elif s == 'i':
            ans = (ans + a) % MOD

    # output
    print(ans)


if __name__ == '__main__':
    main()
