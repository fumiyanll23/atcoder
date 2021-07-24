def main():
    # input
    A, B, N = map(int, input().split())

    # compute
    x = min(B-1, N)

    # output
    print((A*x)//B - A*(x//B))


if __name__ == '__main__':
    main()
