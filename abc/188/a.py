def main():
    # input
    X, Y = map(int, input().split())

    # compute

    # output
    if min(X,Y)+3 > max(X,Y):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
