def main():
    # input
    ABCs = [*map(int, input().split())]

    # compute
    ABCs.sort()

    # output
    print(ABCs[1] + ABCs[2])


if __name__ == '__main__':
    main()
