def main():
    # input
    x, y = map(int, input().split())

    # compute
    lss = [[1,3,5,7,8,10,12], [4,6,9,11], [2]]
    flag = False
    for ls in lss:
        if x in ls and y in ls:
            flag = True

    # output
    print('Yes' if flag else 'No')


if __name__ == '__main__':
    main()
