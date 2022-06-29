from collections import deque

def bfs(s: int, t: int, N: int, adj: list) -> list:
    deq = deque([s])
    dist = [-1] * N
    dist[s] = 0
    while deq:
        v = deq.popleft()
        for i in adj[v]:
            if dist[i] == -1:
                dist[i] = dist[v] + 1
                deq.append(i)
    return dist[t]


def main():
    # input
    N, Q = map(int, input().split())
    abs = [[*map(int, input().split())] for _ in range(N-1)]
    cds = [[*map(int, input().split())] for _ in range(Q)]

    # compute
    adjss = [[] for _ in range(N)]
    for a, b in abs:
        a -= 1
        b -= 1
        adjss[a].append(b)
        adjss[b].append(a)

    # output
    for c, d in cds:
        c -= 1
        d -= 1
        if bfs(c, d, N, adjss)%2 == 0:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
