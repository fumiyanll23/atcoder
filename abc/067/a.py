def main():
    # input
    A, B = map(int, input().split())

    # compute

    # output
    if A%3==0 or B%3==0 or (A+B)%3==0:
        print('Possible')
    else:
        print('Impossible')


if __name__ == '__main__':
    main()
