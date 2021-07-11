def main():
    # input
    N, M = map(int, input().split())
    ABs = [[*map(int, input().split())] for _ in range(M)]

    # compute
    adj = [[] for _ in range(N)]
    for A, B in ABs:
        A -= 1
        B -= 1
        adj[A].append(B)
        adj[B].append(A)
    ans = 0
    for i, vs in enumerate(adj):
        tmp_cnt = 0
        for v in vs:
            if i > v:
                tmp_cnt += 1
        if tmp_cnt == 1:
            ans += 1

    # output
    print(ans)


if __name__ == '__main__':
    main()
