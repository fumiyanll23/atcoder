def main():
    # input
    N, K = map(int, input().split())

    # compute
    ans = 0
    for i in range(1,N+1):
        ans += i*K*100 + K*(K+1)//2

    # output
    print(ans)


if __name__ == '__main__':
    main()
