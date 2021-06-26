def main():
    # input
    W, a, b = map(int, input().split())

    # compute

    # output
    if abs(a-b) <= W:
        print(0)
    else:
        print(abs(a-b) - W)


if __name__ == '__main__':
    main()
