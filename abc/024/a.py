def main():
    # input
    A, B, C, K = map(int, input().split())
    S, T = map(int, input().split())

    # compute
    ans = A*S + B*T
    if S+T >= K:
        ans -= (S+T)*C

    # output
    print(ans)


if __name__ == '__main__':
    main()
