def main():
    # input
    N = int(input())
    tlrss = [[*map(int, input().split())] for _ in range(N)]

    # compute
    for i in range(N):
        if tlrss[i][0] == 1:
            pass
        elif tlrss[i][0] == 2:
            tlrss[i][2] -= 0.5
        elif tlrss[i][0] == 3:
            tlrss[i][1] += 0.5
        else:
            tlrss[i][1] += 0.5
            tlrss[i][2] -= 0.5
    cnt = 0
    for i in range(N-1):
        for j in range(i+1,N):
            t1, l1, r1 = tlrss[i][0], tlrss[i][1], tlrss[i][2]
            t2, l2, r2 = tlrss[j][0], tlrss[j][1], tlrss[j][2]
            if max(l1,l2) <= min(r1,r2):
                cnt += 1

    # output
    print(cnt)


if __name__ == '__main__':
    main()
