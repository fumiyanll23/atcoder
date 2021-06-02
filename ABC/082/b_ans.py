def main():
    # input
    s = input()
    t = input()

    # compute

    # output
    if ''.join(sorted(s)) < ''.join(sorted(t, reverse=True)):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
