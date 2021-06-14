def main():
    # input
    N = int(input())
    hs = [*map(int, input().split())]

    # compute
    hs_min = min(hs)
    cnt = 0
    if hs_min != 0:
        cnt += 1
        for i in range(N):
            hs[i] -= hs_min
    hs.insert(0, 0)
    hs.append(0)
    zeros_idx = []
    for i,h in enumerate(hs):
        if h == 0:
            zeros_idx.append(i)
    for i in range(len(zeros_idx)-1):
        cnt += max(hs[zeros_idx[i]:zeros_idx[i+1]])

    # output
    print(cnt)


if __name__ == '__main__':
    main()
