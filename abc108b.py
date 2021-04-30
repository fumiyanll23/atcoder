def main():
    # input
    x1, y1, x2, y2 = map(int, input().split())

    # compute
    X, Y = x2-x1, y2-y1

    # output
    print(x2-Y, y2+X, x1-Y, y1+X)


if __name__ == '__main__':
    main()
