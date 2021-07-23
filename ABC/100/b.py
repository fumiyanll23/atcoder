def main():
    # input
    D, N = map(int, input().split())

    # compute

    # output
    if D == 0:
        if N < 100:
            print(N)
        else:
            print(101)
    elif D == 1:
        if N < 100:
            print(100 * N)
        else:
            print(10100)
    else:
        if N < 100:
            print(100 * 100 * N)
        else:
            print(1010000)


if __name__ == '__main__':
    main()
