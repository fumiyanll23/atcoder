def main():
    # input
    A, B = map(int, input().split())

    # compute
    if A == 1:
        A += 13
    if B == 1:
        B += 13

    # output
    if A > B:
        print('Alice')
    elif A < B:
        print('Bob')
    else:
        print('Draw')


if __name__ == '__main__':
    main()
