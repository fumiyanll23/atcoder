def main():
    # input
    A, B, N = map(int, input().split())

    # compute
    if N%B == 0:
        x = min(B-1, N-1)
    else:
        x = min(B-1, N)

    # output
    print((A*x)//B - A*(x//B))


if __name__ == '__main__':
    main()
