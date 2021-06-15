def main():
    # input
    N, Y = map(int, input().split())

    # compute
    for i in range(N+1):
        for j in range(N+1):
            if 10000*i+5000*j+1000*(N-i-j)==Y and N-i-j>=0:
                print(i, j, N-i-j)
                exit()

    # output
    print(-1, -1, -1)


if __name__ == '__main__':
    main()
