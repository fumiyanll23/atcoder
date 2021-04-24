def main():
    # input
    N, K = map(int, input().split())
    hs = [int(input()) for _ in range(N)]

    # compute
    n = N-K+1
    diffs = []
    hs.sort()
    for i in range(n):
        diffs.append(hs[i+K-1]-hs[i])

    # output
    print(min(diffs))


if __name__ == '__main__':
    main()
