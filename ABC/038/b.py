def main():
    # input
    HW1s = [*map(int, input().split())]
    HW2s = [*map(int, input().split())]

    # compute
    flag = False
    for HW1 in HW1s:
        for HW2 in HW2s:
            if HW1 == HW2:
                flag = True

    # output
    if flag:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
