def main():
    # input
    S = input()
    chokudai = 'chokudai'
    MOD = 10**9 + 7

    # compute
    cnts = [0] * len(chokudai)
    for i, c in enumerate(S):
        if c in chokudai:
            i = chokudai.index(c)
            if i == 0:
                cnts[0] += 1
            else:
                cnts[i] = (cnts[i] + cnts[i-1]) % MOD

    # output
    print(cnts[-1])


if __name__ == '__main__':
    main()
