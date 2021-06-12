def main():
    # input
    x, y = map(int, input().split())

    # compute
    lss = [0, 1, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1]

    # output
    print('Yes' if lss[x]==lss[y] else 'No')


if __name__ == '__main__':
    main()
