def main():
    # input
    ls = sorted([*map(int, input().split())])

    # compute

    # output
    print(ls[0] if ls[1]==ls[2] else ls[2])


if __name__ == '__main__':
    main()
