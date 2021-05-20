def main():
    # input
    N = int(input())
    As = [int(input()) for _ in range(N)]

    # compute
    light = 0
    cnt = 1
    while cnt != N:
        light = As[light] - 1
        if light == 1:
            print(cnt)
            exit()
        cnt += 1

    # output
    print(-1)


if __name__ == '__main__':
    main()
