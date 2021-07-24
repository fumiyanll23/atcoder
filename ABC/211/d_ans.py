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

    ## BFS + count routes
    deq = deque([0])
    dist = [-1] * N
    cnts = [0] * N
    dist[0] = 0
    cnts[0] = 1
    while deq:
        nxt = deq.popleft()
        for v in adj[nxt]:
            if dist[v] == -1:
                dist[v] = dist[nxt] + 1
                deq.append(v)
                cnts[v] = cnts[nxt]
            elif dist[v] == dist[nxt] + 1:
                cnts[v] = (cnts[v] + cnts[nxt]) % MOD

    # output
    print(cnts[-1])


if __name__ == '__main__':
    main()
