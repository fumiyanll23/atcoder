def main():
    # input
    X, A, B = map(int, input().split())

    # compute

    # output
    if B <= A:
        print('delicious')
    elif B <= A+X:
        print('safe')
    else:
        print('dangerous')


if __name__ == '__main__':
    main()
