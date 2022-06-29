def main():
    # input
    A, D = map(int, input().split())

    # compute
    if A <= D:
        A += 1
    else:
        D += 1

    # output
    print(A * D)


if __name__ == '__main__':
    main()
