from math import floor

def main():
    # input
    X = input()

    # compute
    if '.' in X:
        point = X.index('.')
    else:
        print(int(X))
        exit()

    # output
    print(int(''.join(X[:point])))


if __name__ == '__main__':
    main()
