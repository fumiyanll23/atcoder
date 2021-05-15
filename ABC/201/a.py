def main():
    # input
    As = list(map(int, input().split()))

    # compute
    As.sort()

    # output
    if As[2]-As[1] == As[1]-As[0]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
