def main():
    # input
    N, M, X, Y = map(int, input().split())
    xs = [*map(int, input().split())]
    ys = [*map(int, input().split())]

    # compute
    xs.sort()
    ys.sort()
    for Z in range(X+1, Y+1):
        if xs[-1] < Z <= ys[0]:
            print('No War')
            exit()

    # output
    print('War')


if __name__ == '__main__':
    main()
