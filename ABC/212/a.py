def main():
    # input
    A, B = map(int, input().split())

    # compute

    # output
    if 0 < A and B == 0:
        print('Gold')
    elif A == 0 and 0 < B:
        print('Silver')
    else:
        print('Alloy')


if __name__ == '__main__':
    main()
