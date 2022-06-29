def main():
    # input
    N, K = map(int, input().split())
    ABs = [[*map(int, input().split())] for _ in range(N)]

    # compute
    ABs.sort()
    money = K
    for a,b in ABs:
        if money < a:
            print(money)
            exit()
        else:
            pass
        money += b

    # output
    print(money)


if __name__ == '__main__':
    main()
