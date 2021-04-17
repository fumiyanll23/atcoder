def main():
    # input
    X, Y, Z = map(int, input().split())

    # compute
    price = 10 ** 8
    i = 1
    while not(price/Z < Y/X):
        price -= i

    # output
    print(price)


if __name__ == '__main__':
    main()
