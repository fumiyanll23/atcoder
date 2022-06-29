def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute

    # output
    if len(set(As)) == N:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
