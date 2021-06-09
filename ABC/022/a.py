def main():
    # input
    N, S, T = map(int, input().split())
    W = int(input())
    As = [int(input()) for _ in range(N-1)]

    # compute
    if S <= W <= T:
        ans = 1
    else:
        ans = 0
    for A in As:
        W += A
        if S <= W <= T:
            ans += 1

    # output
    print(ans)


if __name__ == '__main__':
    main()
