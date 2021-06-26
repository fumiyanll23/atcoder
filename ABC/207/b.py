def main():
    # input
    A, B, C, D = map(int, input().split())

    # compute
    cnt = 0
    blue, red = A, 0
    for _ in range(10**8):
        if blue <= D*red:
            print(cnt)
            exit()
        else:
            cnt += 1
            blue += B
            red += C

    # output
    print(-1)


if __name__ == '__main__':
    main()
