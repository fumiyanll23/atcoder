def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute

    # output
    print(max(As) - min(As))


if __name__ == '__main__':
    main()
