def main():
    # input
    s = input()

    # compute
    left = s.index('A')
    right = len(s) - ''.join([*reversed(s)]).index('Z')

    # output
    print(right - left)


if __name__ == '__main__':
    main()
