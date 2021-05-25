def main():
    # input
    N = int(input())
    cs = input()

    # compute
    r = cs.count('R')
    cs1 = cs[:r]

    # output
    print(cs1.count('W'))


if __name__ == '__main__':
    main()
