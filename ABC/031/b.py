def main():
    # input
    L, H = map(int, input().split())
    N = int(input())
    As = [int(input()) for _ in range(N)]

    # compute

    # output
    for A in As:
        if A < L:
            print(L - A)
        elif L <= A <= H:
            print(0)
        else:
            print(-1)


if __name__ == '__main__':
    main()
