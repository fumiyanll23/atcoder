def main():
    # input
    A, B, C = map(int, input().split())

    # compute
    if C%2 == 0:
        A, B = abs(A), abs(B)

    # output
    if A > B:
        print('>')
    elif A < B:
        print('<')
    else:
        print('=')


if __name__ == '__main__':
    main()
