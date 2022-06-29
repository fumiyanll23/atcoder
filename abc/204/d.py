def main():
    # input
    N = int(input())
    Ts = [*map(int, input().split())]

    # compute
    Ts.sort(reverse=True)
    Asum, Bsum = 0, 0
    for T in Ts:
        if Asum > Bsum:
            Bsum += T
        else:
            Asum += T

    # output
    print(max(Asum, Bsum))


if __name__ == '__main__':
    main()
