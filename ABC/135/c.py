def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))

    # compute
    monster = sum(As)
    for i in range(N):
        min_like = min(As[i], Bs[i])
        As[i] -= min_like
        Bs[i] -= min_like
        if Bs[i] != 0:
            min_like = min(As[i+1], Bs[i])
            As[i+1] -= min_like
            Bs[i] -= min_like

    # output
    print(monster-sum(As))


if __name__ == '__main__':
    main()
