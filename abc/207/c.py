def main():
    # input
    N = int(input())
    tlrss = [[*map(int, input().split())] for _ in range(N)]

    # compute
    cnt = 0
    for i in range(N-1):
        for j in range(i+1,N):
            s, a, b = tlrss[i][0], tlrss[i][1], tlrss[i][2]
            t, c, d = tlrss[j][0], tlrss[j][1], tlrss[j][2]
            if b > c:
                print()
                print(i, a, b)
                print(j, c, d)

    # output
    print(cnt)


if __name__ == '__main__':
    main()
