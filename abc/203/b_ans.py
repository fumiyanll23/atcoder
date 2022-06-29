def main():
    # input
    N, K = map(int, input().split())

    # compute

    # output
    print(N*K*(100*(N+1)+(K+1)) // 2)


if __name__ == '__main__':
    main()
