def main():
    # input
    N, K = map(int, input().split())
    ABs = [[*map(int, input().split())] for _ in range(N)]

    # compute
    ABs.sort(key=lambda x: x[0])
    ans = 0
    for i,AB in enumerate(ABs):
        a, b = AB
        move = a-ans
        if K-move < 0:
            ans += K
            K -= K
            break
        else:
            ans += move
            K -= move
            K += b
            if i == N-1:
                ans += K
                K -= K

    # output
    print(ans)


if __name__ == '__main__':
    main()
