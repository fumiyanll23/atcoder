def main():
    # input
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())

    # compute

    # output
    print(X*N if N<K else X*K+Y*(N-K))


if __name__ == '__main__':
    main()
