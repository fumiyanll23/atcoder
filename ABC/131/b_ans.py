def main():
    # input
    N, L = map(int, input().split())

    # compute
    ans = N*L + N*(N-1)//2

    # output
    if 0 <= L:
        print(ans - L)
    elif L+N-1 <= 0:
        print(ans - (L+N-1))
    else:
        print(ans)


if __name__ == '__main__':
    main()
