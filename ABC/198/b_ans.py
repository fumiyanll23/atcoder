def main():
    # input
    N = input()

    # compute
    for i in range(10):
        T = '0'*i + N
        if T == T[::-1]:
            print('Yes')
            exit()

    # output
    print('No')


if __name__ == '__main__':
    main()
