def main():
    # input
    A, B, C = map(int, input().split())

    # compute
    if A+B == C:
        flag1 = True
    else:
        flag1 = False
    if A-B == C:
        flag2 = True
    else:
        flag2 = False

    # output
    if flag1 and flag2:
        print('?')
    elif not (flag1 or flag2):
        print('!')
    elif flag1:
        print('+')
    else:
        print('-')


if __name__ == '__main__':
    main()
