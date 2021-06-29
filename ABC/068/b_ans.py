def main():
    # input
    N = int(input())

    # compute
    NUMBERS = [1, 2, 4, 8, 16, 32, 64]

    # output
    print(max([number for number in NUMBERS if number<=N]))


if __name__ == '__main__':
    main()
