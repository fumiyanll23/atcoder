def main():
    # input
    S = input()

    # compute
    for i, s in enumerate(S):
        if i%2 == 0:
            if  s.isupper():
                print('No')
                exit()
        else:
            if s.islower():
                print('No')
                exit()

    # output
    print('Yes')


if __name__ == '__main__':
    main()
