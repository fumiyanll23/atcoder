def main():
    # input
    N, M = map(int, input().split())

    # compute
    towns = [0] * N
    for _ in range(M):
        a, b = map(int, input().split())
        towns[a-1] += 1
        towns[b-1] += 1

    # output
    for bridge in towns:
        print(bridge)


if __name__ == '__main__':
    main()
