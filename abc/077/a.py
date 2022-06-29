def main():
    # input
    s = input()
    t = input()

    # compute

    # output
    if s == ''.join(reversed(t)):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
