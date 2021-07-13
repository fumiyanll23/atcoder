def main():
    # input
    S = input()

    # compute

    # output
    if all([s.islower() if i%2==0 else s.isupper() for i, s in enumerate(S)]):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
