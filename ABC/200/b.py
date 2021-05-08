def main():
    # input
    N, K = map(int, input().split())

    # compute
    for i in range(K):
        if N%200 == 0:
            N //= 200
        else:
            tmp = str(N)
            N = int(tmp+'200')

    # output
    print(int(N))


if __name__ == '__main__':
    main()
