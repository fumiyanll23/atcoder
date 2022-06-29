def main():
    # input
    A = [*map(int, input())]
    B = [*map(int, input())]

    # compute
    if len(A) > len(B):
        print('GREATER')
        exit()
    elif len(A) < len(B):
        print('LESS')
        exit()
    elif len(A) == len(B):
        for a,b in zip(A,B):
            if a > b:
                print('GREATER')
                exit()
            elif a < b:
                print('LESS')
                exit()

    # output
    print('EQUAL')


if __name__ == '__main__':
    main()
