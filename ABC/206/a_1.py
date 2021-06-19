def main():
    # input
    N = int(input())

    # compute
    N = int(1.08*N)

    # output
    if N < 206:
        print('Yay!')
    elif N == 206:
        print('so-so')
    else:
        print(':(')


if __name__ == '__main__':
    main()
