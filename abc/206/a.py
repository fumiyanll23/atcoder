from math import floor

def main():
    # input
    N = int(input())

    # compute

    # output
    if floor(1.08*N) < 206:
        print('Yay!')
    elif floor(1.08*N) == 206:
        print('so-so')
    else:
        print(':(')


if __name__ == '__main__':
    main()
