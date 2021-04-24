def main():
    # input
    N, K = map(int, input().split())
    hs = [int(input()) for _ in range(N)]

    # compute
    cnts = [0] * 10**9
    trees = []
    for hight in sorted(hs):
        cnts[hight] += 1
    for i,cnt in enumerate(cnts):
        if cnt >= K:
            print(0)
            exit()
        else:
            for _ in range(cnt):
                trees.append(i)

    # output
    print(max(trees) - min(trees))


if __name__ == '__main__':
    main()
