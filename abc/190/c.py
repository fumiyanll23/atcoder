def main():
    # input
    N, M = map(int, input().split())
    ABs = []
    for _ in range(M):
        ABs.append(list(map(int, input().split())))
    K = int(input())
    CDs = []
    for _ in range(K):
        CDs.append(list(map(int, input().split())))

    # compute
    ans = 0
    for i in range(2**K):
        dishes = [0 for _ in range(N)]
        for j in range(K):
            if (i>>j) & 1:
                dishes[CDs[j][1]-1] += 1
            else:
                dishes[CDs[j][0]-1] += 1
        cnt = 0
        for j in range(M):
            if dishes[ABs[j][0]-1]>=1 and dishes[ABs[j][1]-1]>=1:
                cnt += 1
        ans = max(ans, cnt)

    # output
    print(ans)


if __name__ == '__main__':
    main()
