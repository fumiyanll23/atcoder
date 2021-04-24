def main():
    # input
    N = int(input())
    S = input()
    Q = int(input())
    TABss = [list(map(int, input().split())) for _ in range(Q)]

    # compute
    s1, s2 = S[:N], S[N:]
    for i in range(Q):
        if TABss[i][0] == 1:
            A, B = TABss[i][1]-1, TABss[i][2]-1
            if A < B < N:
                tmp1 = s1[:A]+s1[B]+s1[A+1:B]+s1[A]+s1[B+1:]
                tmp2 = s2
            elif A < N <= B:
                B -= N
                tmp1 = s1[:A]+s2[B]+s1[A+1:]
                tmp2 = s2[:B]+s1[A]+s2[B+1:]
            elif N <= A < B :
                A -= N
                B -= N
                tmp1 = s1
                tmp2 = s2[:A]+s2[B]+s2[A+1:B]+s2[A]+s2[B+1:]
        else:
            tmp1, tmp2 = s2, s1
        s1, s2 = tmp1, tmp2

    # output
    print(s1+s2)


if __name__ == '__main__':
    main()
