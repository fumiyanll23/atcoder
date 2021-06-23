def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    ans = 0
    for i in range(N-1):
        for j in range(i,N):
            tmp_min = min(As[i:j+1])
            tmp_orange = tmp_min * (j-i+1)
            if ans < tmp_orange:
                ans = tmp_orange

    # output
    print(ans)


if __name__ == '__main__':
    main()
