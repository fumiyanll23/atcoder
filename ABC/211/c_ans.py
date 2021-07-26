def main():
    # input
    S = input()
    T = 'chokudai'
    MOD = 10**9 + 7

    # compute
    cnts = [0] * len(T)
    for i, s in enumerate(S):
        if s in T:
            i = T.index(s)
            if i == 0:
                cnts[0] += 1
            else:
                cnts[i] = (cnts[i] + cnts[i-1]) % MOD

    # output
    print(cnts[-1])


if __name__ == '__main__':
    main()
