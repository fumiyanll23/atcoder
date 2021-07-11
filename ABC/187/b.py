def main():
    # input
    N = int(input())
    xys = [[*map(int, input().split())] for _ in range(N)]

    # compute
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            xi, yi = xys[i][0], xys[i][1]
            xj, yj = xys[j][0], xys[j][1]
            if abs(yi-yj) <= abs(xi-xj):
                ans += 1

    # output
    print(ans)


if __name__ == '__main__':
    main()
