def main():
    # input
    A, B = map(int, input().split())

    # compute
    ans = ''
    if A < B:
        if A == 1:
            ans = 'Alice'
        else:
            ans = 'Bob'
    elif A > B:
        if B == 1:
            ans = 'Bob'
        else:
            ans = 'Alice'
    else:
        ans = 'Draw'

    # output
    print(ans)


if __name__ == '__main__':
    main()
