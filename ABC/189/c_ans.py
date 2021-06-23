def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    ans = 0
    for l in range(N):
        x = As[l]
        for r in range(l,N):
            x = min(x, As[r])
            ans = max(ans, x*(r-l+1))

    # output
    print(ans)


if __name__ == '__main__':
    main()
