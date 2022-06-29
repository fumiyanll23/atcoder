def main():
    # input
    N = int(input())
    hs = [*map(int, input().split())]

    # compute
    cnt = hs[0]
    for i in range(1,N):
        if hs[i-1] < hs[i]:
            cnt += hs[i] - hs[i-1]

    # output
    print(cnt)


if __name__ == '__main__':
    main()
