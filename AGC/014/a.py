def main():
    # input
    ABCs = list(map(int, input().split()))

    # compute
    cnt = 0
    while not(ABCs[0]%2==1 or ABCs[1]%2==1 or ABCs[2]%2==1):
        cnt += 1
        tmps = list(ABCs)
        ABCs[0] = (tmps[1]+tmps[2]) // 2
        ABCs[1] = (tmps[2]+tmps[0]) // 2
        ABCs[2] = (tmps[0]+tmps[1]) // 2
        if cnt >= 10**7:
            print(-1)
            exit()

    # output
    print(cnt)


if __name__ == '__main__':
    main()
