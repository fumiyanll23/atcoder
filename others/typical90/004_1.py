def main():
    # input
    H, W = map(int, input().split())
    Ass = [[*map(int, input().split())] for _ in range(H)]

    # compute
    sumH = [0]*W
    sumW = [0]*H
    for i in range(H):
        for j in range(W):
            sumH[j] += Ass[i][j]
            sumW[i] += Ass[i][j]

    # output
    for i in range(H):
        print(*[sumW[i] + sumH[j] - Ass[i][j]  for j in range(W)])


if __name__ == '__main__':
    main()
