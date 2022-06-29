def main():
    # input
    N, X = map(int, input().split())
    VPs = [list(map(int, input().split())) for _ in range(N)]

    # compute
    alchol = 0
    X *= 100
    for i,vp in enumerate(VPs):
        alchol += vp[0] * vp[1]
        if alchol > X:
            print(i+1)
            exit()

    # output
    print(-1)


if __name__ == '__main__':
    main()
