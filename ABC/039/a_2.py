def main():
    # input
    ABCs = [*map(int, input().split())]

    # compute

    # output
    print(2 * sum([ABCs[i-1]*ABCs[i] for i in range(3)]))


if __name__ == '__main__':
    main()
