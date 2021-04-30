from itertools import permutations

def main():
    # input
    N, K = map(int, input().split())
    Tss = [list(map(int, input().split())) for _ in range(N)]

    # compute
    cnt = 0
    for cities in permutations(range(1,N), N-1):
        time = Tss[0][cities[0]]
        for i in range(N-2):
            time += Tss[cities[i]][cities[i+1]]
        time += Tss[cities[-1]][0]
        if time == K:
            cnt += 1

    # output
    print(cnt)


if __name__ == '__main__':
    main()
