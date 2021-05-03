def main():
    # input
    H, W = map(int, input().split())
    sss = [input() for _ in range(H)]

    # compute
    cnt = 0
    for h in range(1,H-1):
        for w in range(1,W-1):
            if sss[h][w]=='#' and sss[h-1][w]!='#' and sss[h+1][w]!='#' and sss[h][w-1]!='#' and sss[h][w+1]!='#':
                cnt += 1

    # output
    if cnt == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
