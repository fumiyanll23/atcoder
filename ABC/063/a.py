def main():
    # input
    ABs = [*map(int, input().split())]

    # compute

    # output
    print('error' if sum(ABs)>=10 else sum(ABs))


if __name__ == '__main__':
    main()
