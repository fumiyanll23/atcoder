def main():
    # input
    x, a, b = map(int, input().split())

    # compute

    # output
    if abs(x-a) < abs(x-b):
        print('A')
    else:
        print('B')


if __name__ == '__main__':
    main()
