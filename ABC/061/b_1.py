def main():
    # input
    N, M = map(int, input().split())
    abs = [list(map(int, input().split())) for _ in range(M)]

    # compute
    towns = [0] * N
    for ab in abs:
        towns[ab[0]-1] += 1
        towns[ab[1]-1] += 1

    # output
    for bridge in towns:
        print(bridge)


if __name__ == '__main__':
    main()
