def main():
    # input
    N, M = map(int, input().split())
    Ls = [0] * M
    Rs = [0] * M
    for i in range(M):
        Ls[i], Rs[i] = map(int, input().split())

    # compute

    # output
    print(max(0, min(Rs) - max(Ls) + 1))


if __name__ == '__main__':
    main()
