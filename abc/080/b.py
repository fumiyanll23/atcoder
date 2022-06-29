def main():
    # input
    N = int(input())

    # compute

    # output
    if N%sum([int(n) for n in str(N)]) == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
