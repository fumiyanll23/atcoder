def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    As.sort()

    # output
    print(sum(As[N:3*N-1:2]))


if __name__ == '__main__':
    main()
