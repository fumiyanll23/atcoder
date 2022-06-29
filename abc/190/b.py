def main():
    # input
    N, S, D = map(int, input().split())
    XYs = [[*map(int, input().split())] for _ in range(N)]

    # compute
    for X, Y in XYs:
        if X<S and D<Y:
            print('Yes')
            exit()

    # output
    print('No')


if __name__ == '__main__':
    main()
