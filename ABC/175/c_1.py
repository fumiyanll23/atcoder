def main():
    # input
    X, K, D = map(int, input().split())

    # compute
    X = abs(X)

    # output
    if X//D > K:
        print(X - D*K)
    else:
        if (K-X//D)%2 == 0:
            print(X % D)
        else:
            print(min(D-X%D, X%D+D))


if __name__ == '__main__':
    main()
