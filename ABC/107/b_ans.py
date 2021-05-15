def main():
    # input
    H, W = map(int, input().split())
    ass = [list(input()) for _ in range(H)]

    # compute
    rows = [False] * H
    columns = [False] * W
    for i in range(H):
        for j in range(W):
            if ass[i][j] == '#':
                rows[i] = True
                columns[j] = True

    # output
    for i in range(H):
        if rows[i]:
            for j in range(W):
                if columns[j]:
                    print(ass[i][j], end='')
            print()


if __name__ == '__main__':
    main()
