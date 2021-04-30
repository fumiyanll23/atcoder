from itertools import product

def main():
    # input
    N, M = map(int, input().split())
    ABs = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CDs = [list(map(int, input().split())) for _ in range(K)]

    # compute
    cnt_max = 0
    for number in product(*CDs):
        dishes = [0] * N
        for i in range(K):
            dishes[number[i]-1] += 1
        cnt = 0
        for i,ab in enumerate(ABs):
            if dishes[ab[0]-1]>=1 and dishes[ab[1]-1]>=1:
                cnt += 1
        cnt_max = max(cnt_max, cnt)

    # output
    print(cnt_max)


if __name__ == '__main__':
    main()
