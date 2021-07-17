def main():
    # input
    N, Q = map(int, input().split())
    LRTs = [[*map(int, input().split())] for _ in range(Q)]

    # compute
    anss = [0] * N
    for L, R, T in LRTs:
        for i in range(L-1, R):
            anss[i] = T

    # output
    for ans in anss:
        print(ans)


if __name__ == '__main__':
    main()
