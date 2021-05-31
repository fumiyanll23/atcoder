def main():
    # input
    N = int(input())
    xys = [[*map(int, input().split())] for _ in range(N)]

    # compute
    xs = [xy[0] for xy in xys]
    xmax, xmin = max(xs), min(xs)
    ys = [xy[1] for xy in xys]
    ymax, ymin = max(ys), min(ys)
    dists = []
    for xy in xys:
        dists.append(max(abs(xy[0]-xmax), abs(xy[0]-xmin), abs(xy[1]-ymax), abs(xy[1]-ymin)))

    # output
    print([*sorted(dists)][-3])


if __name__ == '__main__':
    main()
