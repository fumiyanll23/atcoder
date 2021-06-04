def main():
    # input
    X = input()

    # compute
    if '.' in X:
        X = X[:X.index('.')]

    # output
    print(X)


if __name__ == '__main__':
    main()
