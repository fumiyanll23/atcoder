from collections import deque

def main():
    # input
    N, M = map(int, input().split())
    ABs = [[*map(int, input().split())] for _ in range(M)]

    # compute
    adj = [[] for _ in range(N)]
    for A, B in ABs:
        adj[A-1].append(B-1)
        adj[B-1].append(A-1)
    deq = deque([0])
    dist = [-1] * N
    dist[0] = 0
    while deq:
        v = deq.popleft()
        for nxt in adj[v]:
            if dist[nxt] == -1:
                dist[nxt] = dist[v] + 1
                deq.append(nxt)

    # output
    if dist[-1] == 2:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')


if __name__ == '__main__':
    main()
