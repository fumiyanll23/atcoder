def main():
    # input
    N, M = map(int, input().split())
    ABCs = [[*map(int, input().split())] for _ in range(M)]

    # compute
    ## 各頂点への距離を格納するリストdistの初期化
    INF = 1 << 60
    dist = [[INF]*N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for A, B, C in ABCs:
        dist[A-1][B-1] = C

    ans = 0
    for k in range(N):
        nxt = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                nxt[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
                if nxt[i][j] < 1<<59:
                    ans += nxt[i][j]
        dist = nxt

    # output
    print(ans)


if __name__ == '__main__':
    main()
