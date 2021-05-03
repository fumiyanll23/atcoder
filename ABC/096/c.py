def main():
    # input
    H, W = map(int, input().split())
    sss = [list(input()) for _ in range(H)]

    # compute
    tss = [['.']*W for _ in range(H)]
    for h in range(H-1):
        for w in range(W):
            if sss[h][w] == sss[h+1][w] == '#':
                tss[h][w], tss[h+1][w] = '#', '#'
    for h in range(H):
        for w in range(W-1):
            if sss[h][w] == sss[h][w+1] == '#':
                tss[h][w], tss[h][w+1] = '#', '#'

    # output
    if sss == tss:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
