def main():
    # input
    N, M = map(int, input().split())

    # compute
    ans = min(N, M//2)
    M -= 2 * ans
    ans += M // 4

    # output
    print(ans)


if __name__ == '__main__':
    main()
