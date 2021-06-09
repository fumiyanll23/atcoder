def main():
    # input
    H, W = map(int, input().split())
    Ass = [[*map(int, input().split())] for _ in range(H)]

    # compute
    ansss = []
    for i in range(H):
        ansss.append([sum(Ass[i])] * W)
    for j in range(W):
        tmp_sum = 0
        for i in range(H):
            tmp_sum += Ass[i][j]
        for i in range(H):
            ansss[i][j] += tmp_sum
    for i in range(H):
        for j in range(W):
            ansss[i][j] -= Ass[i][j]

    # output
    for i in range(H):
        print(*ansss[i])


if __name__ == '__main__':
    main()
