def main():
    # input
    a, b, c = map(int, input().split())

    # compute

    # output
    print('Yes' if a+b==c or b+c==a or c+a==b else 'No')


if __name__ == '__main__':
    main()
