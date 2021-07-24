from collections import deque, defaultdict

def main():
    # input
    N, M = map(int, input().split())
    ABs = [[*map(int, input().split())] for _ in range(M)]
    MOD = 10**9 + 7

    # compute
    adj = [[] for _ in range(N)]
    for A, B in ABs:
        adj[A-1].append(B-1)
        adj[B-1].append(A-1)

    ## BFS
    deq = deque([0])
    dist = [-1] * N
    dist[0] = 0
    while deq:
        nxt = deq.popleft()
        for v in adj[nxt]:
            if dist[v] == -1:
                dist[v] = dist[nxt] + 1
                deq.append(v)

    ## count routes
    ddict = defaultdict(int)
    for d in dist:
        ddict[d] += 1
    ans = 1
    if dist[N-1] == -1:
        ans = 0
    else:
        for v in ddict.values():
            ans = ans * v % MOD

    # output
    print(ans)


if __name__ == '__main__':
    main()
