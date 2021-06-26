def main():
    # input
    W, a, b = map(int, input().split())

    # compute

    # output
    if a+W < b:
        print(b - (a+W))
    elif b+W < a:
        print(a - (b+W))
    else:
        print(0)


if __name__ == '__main__':
    main()
