def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    As.sort()
    ans = 0
    for i in range(N-1):
        ans += As[i+1] - As[i]

    # output
    print(ans)


if __name__ == '__main__':
    main()
