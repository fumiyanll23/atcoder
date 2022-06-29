def main():
    # input
    N = int(input())
    xs, ys = [0]*N, [0]*N
    for i in range(N):
        xs[i], ys[i] = map(int, input().split())

    # compute
    xs.sort(reverse=True)
    ys.sort(reverse=True)
    pxs = [xs[0], xs[1], xs[-2], xs[-1]]
    pys = [ys[0], ys[1], ys[-2], ys[-1]]
    dists_x, dists_y = [], []
    for i in range(3):
        for j in range(i,4):
            dists_x.append(abs(pxs[i]-pxs[j]))
            dists_y.append(abs(pys[i]-pys[j]))
    totals = dists_x + dists_y
    totals.sort(reverse=True)

    # output
    print(totals[1])


if __name__ == '__main__':
    main()
