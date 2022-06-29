def main():
    # input
    L, R = map(int, input().split())
    MOD = 2019

    # compute
    flag_3 = False
    flag_673 = False
    s, t = L//3, R//3
    for i in range(s-1, t+1):
        if L <= 2019*i <= R:
            print(0)
            exit()
        if L <= 3*i <= R:
            flag_3 = True
        if L <= 673*i <= R:
            flag_673 = True
            if flag_3 and flag_673:
                print(0)
                exit()

    # output
    print(L * (L+1) % MOD)


if __name__ == '__main__':
    main()
