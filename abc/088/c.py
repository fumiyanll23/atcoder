def main():
    # input
    css = [[*map(int, input().split())] for _ in range(3)]

    # compute
    for i in range(3):
        if css[i-1][i-1]+css[i][i] != css[i-1][i]+css[i][i-1]:
            print('No')
            exit()

    # output
    print('Yes')


if __name__ == '__main__':
    main()
