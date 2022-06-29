import sys
sys.setrecursionlimit(10**4)

def main():
    # input
    N, M = map(int, input().split())
    Gss = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        Gss[A-1].append(B-1)

    # compute
    ans = 0


    def dfs(v: int) -> None:
        if temp[v]:
            return
        temp[v] = True
        for vv in Gss[v]:
            dfs(vv)


    for i in range(N):
	    temp = [False] * N
	    dfs(i)
	    ans += sum(temp)

    # output
    print(ans)


if __name__ == '__main__':
    main()
