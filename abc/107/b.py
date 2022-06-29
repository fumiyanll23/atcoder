def main():
    # input
    H, W = map(int, input().split())
    ass = [list(input()) for _ in range(H)]

    # compute
    for i in range(H):
        if ass[i] == ['.']*W:
            ass[i] = [''] * W

    for j in range(W):
        cnt = 0
        for i in range(H):
            if ass[i][j]=='.' or ass[i][j]=='':
                cnt += 1
        if cnt == H:
            for k in range(H):
                ass[k][j] = ''

    # output
    for As in ass:
        if ''.join(As) != '':
            print(''.join(As))


if __name__ == '__main__':
    main()
