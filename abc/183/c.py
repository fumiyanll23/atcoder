import itertools

def main():
    # input
    N, K = map(int, input().split())
    Tss = [list(map(int, input().split())) for _ in range(N)]

    # compute
    cnt = 0
    routes = list(itertools.permutations(range(1, N), N-1))
    for i in routes:
        total = Tss[0][i[0]]
        for j in range(1, N-1):
            total += Tss[i[j-1]][i[j]]
        total += Tss[i[-1]][0]
        if total == K:
            cnt += 1

    # output
    print(cnt)


if __name__ == '__main__':
    main()
