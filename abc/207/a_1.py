def main():
    # input
    ABCs = [*map(int, input().split())]

    # compute
    A, B, C = sorted(ABCs)

    # output
    print(B + C)


if __name__ == '__main__':
    main()
