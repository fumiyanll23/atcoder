def main():
    # input
    A, B, C, D = map(int, input().split())

    # compute
    All = B - A + 1
    c = All // C
    d = All // D
    cd = All // (C*D)

    # output
    print(All-c-d+cd)


if __name__ == '__main__':
    main()
