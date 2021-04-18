def main():
    # input
    X, Y = map(int, input().split())

    # compute

    # output
    if Y == 0:
        print('ERROR')
    else:
        print(f'{X//Y}.{(X*100//Y)%100:02d}')

if __name__ == '__main__':
    main()
