def main():
    # input
    N = int(input())

    # compute
    l_0, l_1 = 2, 1
    if N == 1:
        print(l_1)
    else:
        for _ in range(N-1):
            l_i = l_0 + l_1
            l_0, l_1 = l_1, l_i
        print(l_i)

    # output


if __name__ == '__main__':
    main()
