def main():
    # input
    S = input()

    # compute
    N = len(S)
    S1, S2 = [0]*(N+1), [0]*(N+1)
    for i in range(N):
        if S[i] == '<':
            S1[i+1] = S1[i] + 1
    for i in reversed(range(N)):
        if S[i] == '>':
            S2[i] = S2[i+1] + 1
    ans = 0
    for s1,s2 in zip(S1,S2):
        ans += max(s1, s2)

    # output
    print(ans)


if __name__ == '__main__':
    main()
