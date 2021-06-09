def main():
    # input
    N = int(input())

    # compute
    one = N % 2
    two = N // 2

    # output
    print(one + two)
    for _ in range(one):
        print(1)
    for _ in range(two):
        print(2)


if __name__ == '__main__':
    main()
