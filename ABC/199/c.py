def main():
    # input
    N = int(input())
    S = input()
    Q = int(input())
    TABss = [list(map(int, input().split())) for _ in range(Q)]

    # compute
    for i in range(Q):
        if TABss[i][0] == 1:
            A, B = TABss[i][1]-1, TABss[i][2]-1
            tmp = S[:A]+S[B]+S[A+1:B]+S[A]+S[B+1:]
        else:
            tmp = S[N:]+S[:N]
        S = tmp

    # output
    print(S)


if __name__ == '__main__':
    main()
