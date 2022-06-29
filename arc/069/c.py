def main():
    # input
    N, M = map(int, input().split())

    # compute
    ans = 0
    if 2*N <= M:
        ans += N
        M -= 2 * N
        ans += M // 4
    else:
        ans += M // 2

    # output
    print(ans)


if __name__ == '__main__':
    main()
