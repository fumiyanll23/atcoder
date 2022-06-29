def main():
    # input
    A, B, C = map(int, input().split())

    # compute

    # output
    if A+B == A-B == C:
        print('?')
    elif A+B == C:
        print('+')
    elif A-B == C:
        print('-')
    else:
        print('!')


if __name__ == '__main__':
    main()
