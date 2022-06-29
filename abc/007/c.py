from collections import deque

def main():
    # input
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    cs = [[*input()] for _ in range(R)]

    # compute
    sy -= 1
    sx -= 1
    gy -= 1
    gx -= 1
    deq = deque([[sy, sx]])
    dist = [[-1 for _ in range(C)] for _ in range(R)]
    dist[sy][sx] = 0
    route = 0
    while deq:
        y, x = deq.popleft()
        tmp_dist = dist[y][x]
        for dy, dx in [[-1,0], [0,1], [1,0], [0,-1]]:
            if y+dy==gy and x+dx==gx:
                route = tmp_dist + 1
                print(route)
                exit()
            elif cs[y+dy][x+dx]=='.' and dist[y+dy][x+dx]==-1:
                dist[y+dy][x+dx] = tmp_dist + 1
                deq.append([y+dy, x+dx])

    # output


if __name__ == '__main__':
    main()
