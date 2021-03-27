# ABC197B - Visibility

def main():
    # input
    H, W, X, Y = map(int, input().split())
    Ss = []
    for _ in range(H):
        Ss.append(str(input()))

    # compute
    X -= 1
    Y -= 1
    i, j, cnt = 0, 0, -3

    while X-i >= 0:
        if Ss[X-i][Y] == '.':
            cnt += 1
        else:
            break
        i += 1
    while Y-j >= 0:
        if Ss[X][Y-j] == '.':
            cnt += 1
        else:
            break
        j += 1

    i, j = 0, 0
    while X+i < H:
        if Ss[X+i][Y] == '.':
            cnt += 1
        else:
            break
        i += 1
    while Y+j < W:
        if Ss[X][Y+j] == '.':
            cnt += 1
        else:
            break
        j += 1

    # output
    print(cnt)


if __name__ == '__main__':
    main()
