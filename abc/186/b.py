def main():
    # input
    H, W = map(int, input().split())
    Ass = [[*map(int, input().split())] for _ in range(H)]

    # compute
    minimum = min([min(As) for As in Ass])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += Ass[i][j] - minimum

    # output
    print(ans)


if __name__ == '__main__':
    main()
