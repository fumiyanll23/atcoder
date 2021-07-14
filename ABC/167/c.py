from itertools import combinations

def main():
    # input
    N, M, X = map(int, input().split())
    CAss = [[*map(int, input().split())] for _ in range(N)]

    # compute
    INF = float('inf')
    ans = INF
    for i in range(1,N+1):
        for comb in combinations(CAss, i):
            tmp_cost = 0
            tmp_skills = [0] * M
            for com in comb:
                for j in range(M+1):
                    if j == 0:
                        tmp_cost += com[j]
                    else:
                        tmp_skills[j-1] += com[j]
            if all([tmp_skill>=X for tmp_skill in tmp_skills]):
                ans = min(ans, tmp_cost)

    # output
    if ans != INF:
        print(ans)
    else:
        print(-1)


if __name__ == '__main__':
    main()
