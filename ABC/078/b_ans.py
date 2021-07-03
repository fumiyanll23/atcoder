def main():
    # input
    X, Y, Z = map(int, input().split())

    # compute
    X -= Z
    ans = 0
    while X-Y-Z >= 0:
        ans += 1
        X -= Y + Z

    # output
    print(ans)


if __name__ == '__main__':
    main()
