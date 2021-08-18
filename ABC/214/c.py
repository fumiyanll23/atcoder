def main():
    # input
    N = int(input())
    Ss = [*map(int, input().split())]
    Ts = [*map(int, input().split())]

    # compute
    now = min(Ts)
    idx = Ts.index(now)
    dp = [[idx, now]]
    while len(dp) != N:
        dp.append([(idx+1)%N, min(now+Ss[idx], Ts[(idx+1)%N])])
        now = dp[-1][1]
        idx = (idx+1) % N
    dp.sort()

    # output
    for ans in dp:
        print(ans[1])


if __name__ == '__main__':
    main()
