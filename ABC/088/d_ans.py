from collections import deque

def main():
    # input
    H, W = map(int, input().split())
    ss = [[*input()] for _ in range(H)]

    # compute
    ## count white squres
    white = 0
    for s in ss:
        for char in s:
            if char == '.':
                white += 1

    ## surround the maze by walls
    for i in range(H):
        ss[i].insert(0, '#')
        ss[i].append('#')
    ss.insert(0, ['#']*(W+2))
    ss.append(['#']*(W+2))

    ## BFS
    ### start
    sy, sx = 1, 1
    ### goal
    gy, gx = H, W
    deq = deque([[sy, sx]])
    dist = [[-1 for _ in range(W+2)] for _ in range(H+2)]
    dist[sy][sx] = 0
    route = 0
    while deq:
        y, x = deq.popleft()
        tmp_dist = dist[y][x]
        for dy, dx in [[-1,0], [0,1], [1,0], [0,-1]]:
            if y+dy==gy and x+dx==gx:
                route = tmp_dist + 1
                print(white - route-1)
                exit()
            elif ss[y+dy][x+dx]=='.' and dist[y+dy][x+dx]==-1:
                dist[y+dy][x+dx] = tmp_dist + 1
                deq.append([y+dy, x+dx])

    # output
    print(-1)


if __name__ == '__main__':
    main()
