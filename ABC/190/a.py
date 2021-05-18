def main():
    # input
    A, B, C = map(int, input().split())

    # compute

    # output
    if A>B or (A==B and C==1):
        print('Takahashi')
    else:
        print('Aoki')


if __name__ == '__main__':
    main()
