def main():
    # input
    N = int(input())
    APXs = [[*map(int, input().split())] for _ in range(N)]

    # compute
    ans = 10**9 + 1
    for A, P, X in APXs:
        if X-A>0 and P<ans:
            ans = P

    # output
    if ans != 10**9+1:
        print(ans)
    else:
        print(-1)


if __name__ == '__main__':
    main()
