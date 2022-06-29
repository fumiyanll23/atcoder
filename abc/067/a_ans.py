def main():
    # input
    A, B = map(int, input().split())

    # compute

    # output
    if A%3==B%3 and A%3:
        print('Impossible')
    else:
        print('Possible')


if __name__ == '__main__':
    main()
