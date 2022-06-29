from collections import deque

def main():
    # input
    N, M = map(int, input().split())
    ABs = [[*map(int, input().split())] for _ in range(M)]

    # compute
    adjss = [[] for _ in range(N)]
    for A,B in ABs:
        adjss[A-1].append(B-1)
        adjss[B-1].append(A-1)
    ### 全ての頂点を未訪問とする
    dists = [-1] * N
    ### 連結成分の個数
    cnt = 0

    ## BFS
    for vi in range(N):
        ### viが未訪問のとき
        if dists[vi] == -1:
            ### viを訪問済みにする
            dists[vi] = 0
            ### viを探索対象とする
            q = deque([vi])
            ### 探索対象である頂点に対してループを回す
            while q:
                ### viを探索していくため、viを探索対象から外す
                vi = q.popleft()
                ### viと隣接するようなvjに対してループを回す
                for vj in adjss[vi]:
                    ### vjが未訪問のとき
                    if dists[vj] == -1:
                        ### vjはviよりも1だけ深い階層にある
                        dists[vj] = dists[vi] + 1
                        ### vjを次の探索対象とする
                        q.append(vj)
            cnt += 1

    # output
    print(cnt - 1)


if __name__ == '__main__':
    main()
