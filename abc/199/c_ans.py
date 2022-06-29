def main():
    # input
    N = int(input())
    S = list(input())
    Q = int(input())
    TABss = [list(map(int, input().split())) for _ in range(Q)]

    # compute
    s1, s2 = S[:N], S[N:]
    for t, a, b in TABss:
        if t == 1:
            a -= 1
            b -= 1
            if a < b < N:
                s1[a], s1[b] = s1[b], s1[a]
            elif a < N <= b:
                b -= N
                s1[a], s2[b] = s2[b], s1[a]
            else:
                a -= N
                b -= N
                s2[a], s2[b] = s2[b], s2[a]
        else:
            s1, s2 = s2, s1

    # output
    print(''.join(s1+s2))

if __name__ == '__main__':
    main()
