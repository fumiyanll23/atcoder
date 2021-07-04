from heapq import heappush, heappop

INF = 10**6 + 1

def dijkstra(s: int, n: int, adj: list) -> list: # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]: # ノード v に隣接しているノードに対して
            if seen[to]:
                continue
            if dist[v]+cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


def main():
    # input
    N, M = map(int, input().split())
    ABCss = [[*map(int, input().split())] for _ in range(M)]

    # compute
    adjss = [[] for _ in range(N)]
    for ABCs in ABCss:
        A, B, C = ABCs
        adjss[A-1].append([B-1, C])

    # output
    for i in range(N):
        for k in range(N):
            ds = dijkstra(i, N, adjss)
            for i in range(N):
                if ds[i] == INF:
                    ds[i] = 0
            print(ds)


if __name__ == '__main__':
    main()
