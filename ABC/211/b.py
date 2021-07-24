def main():
    # input
    Ss = [input() for _ in range(4)]

    # compute
    setSs = set(Ss)

    # output
    if 'H' in setSs and '2B' in setSs and '3B' in setSs and 'HR' in setSs:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
