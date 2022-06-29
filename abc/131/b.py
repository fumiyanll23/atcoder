def main():
    # input
    N, L = map(int, input().split())

      # compute
    delicious = L*N + N*(N-1)//2

    # output
    if L<0 and L+N-1<0:
        print(delicious - (L+N-1))
    elif L>0 and L+N-1>0:
        print(delicious - L)
    else:
        print(delicious)


if __name__ == '__main__':
    main()
