def main():
    # input
    N, Q = map(int, input().split())
    As = [*map(int, input().split())]
    Txyss = [[*map(int, input().split())] for _ in range(Q)]

    # compute
    shift = 0

    # output
    for T, x, y in Txyss:
        if T == 1:
            x = x - 1 - shift
            if x < 0:
                x += N
            y = y - 1 - shift
            if y < 0:
                y += N
            As[x], As[y] = As[y], As[x]
        elif T == 2:
            shift += 1
        else:
            x = x - 1 - shift
            if x < 0:
                x += N
            print(As[x])


if __name__ == '__main__':
    main()
