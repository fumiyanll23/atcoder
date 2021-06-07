def main():
    # input
    A, B, C = map(int, input().split())

    # compute
    for i in range(100000):
        if (A*i)%B == C:
            print('YES')
            exit()

    # output
    print('NO')


if __name__ == '__main__':
    main()
