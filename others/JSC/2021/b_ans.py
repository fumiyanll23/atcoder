def main():
    # input
    N, M = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    # compute

    # output
    print(*sorted(A^B))


if __name__ == '__main__':
    main()
