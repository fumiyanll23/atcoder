def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))

    # compute
    cnt = 0
    for i in range(N):
        cnt += min(As[i], Bs[i])
        As[i], Bs[i] = max(0, As[i]-Bs[i]), max(0, Bs[i]-As[i])
        cnt += min(As[i+1], Bs[i])
        As[i+1], Bs[i] = max(0, As[i+1]-Bs[i]), max(0, Bs[i]-As[i+1])

    # output
    print(cnt)


if __name__ == '__main__':
    main()
