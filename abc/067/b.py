def main():
    # input
    N, K = map(int, input().split())
    ls = [*map(int, input().split())]

    # compute
    ls.sort()
    ans = 0
    for i in range(K):
        ans += ls[-i-1]

    # output
    print(ans)


if __name__ == '__main__':
    main()
