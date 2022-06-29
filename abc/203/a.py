def main():
    # input
    a, b, c = map(int, input().split())

    # compute

    # output
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    elif a!=b and b!=c:
        print(0)


if __name__ == '__main__':
    main()
