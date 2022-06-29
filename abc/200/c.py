def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    cnt = 0
    As.sort()
    for i in range(N-1):
        for j in range(i+1,N):
            if (As[j]-As[i])%200 == 0:
                cnt += 1

    # output
    print(cnt)


if __name__ == '__main__':
    main()
