def main():
    # input
    A, B = map(int, input().split())

    # compute

    # output
    if B == 0:
        print('Gold')
    elif A == 0:
        print('Silver')
    else:
        print('Alloy')


if __name__ == '__main__':
    main()
