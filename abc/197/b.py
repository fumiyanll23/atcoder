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
    i, j, cnt = 0, 0, 0

    while X-i >= 0:
        if Ss[X-i][Y] == '#':
            break
        else:
            cnt += 1
        i += 1


    i = 0
    while X+i < H:
        if Ss[X+i][Y] == '#':
            break
        else:
            cnt += 1
        i += 1


    while Y-j >= 0:
        if Ss[X][Y-j] == '#':
            break
        else:
            cnt += 1
        j += 1


    j = 0
    while Y+j < W:
        if Ss[X][Y+j] == '#':
            break
        else:
            cnt += 1
        j += 1


    # output
    print(cnt - 3)


if __name__ == '__main__':
    main()
