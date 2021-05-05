def main():
    # input
    X, K, D = map(int, input().split())

    # compute

    # output
    if X > 0:
        if X//D > K:
            print(X - D*K)
        else:
            if (K-X//D)%2 == 0:
                print(X % D)
            else:
                print(min(D-X%D, X%D+D))
    else:
        if abs(X)//D > K:
            print(abs(X+D*K))
        else:
            if (K-abs(X)//D)%2 == 0:
                print(abs(X) % D)
            else:
                print(min(D-abs(X)%D, abs(X)%D+D))


if __name__ == '__main__':
    main()
