def main():
    # input
    L, R = map(int, input().split())
    MOD = 2019

    # compute
    ans = 2019
    for i in range(L, R):
        for j in range(i+1, R+1):
            if i*j%MOD == 0:
                print(0)
                exit()
            else:
                ans = min(ans, i*j%MOD)

    # output
    print(ans)


if __name__ == '__main__':
    main()
