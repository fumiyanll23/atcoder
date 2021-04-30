def main():
    # input
    ABCs = list(map(int, input().split()))

    # compute
    cnt = 0
    while not(ABCs[0]==ABCs[1]==ABCs[2]):
        ABCs.sort()
        if (ABCs[2]-ABCs[0])%2 == 0:
            ABCs[0] += 2
            cnt += 1
        else:
            ABCs[0] += 1
            ABCs[1] += 1
            cnt += 1

    # output
    print(cnt)


if __name__ == '__main__':
    main()
