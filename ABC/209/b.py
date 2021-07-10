def main():
    # input
    N, X = map(int, input().split())
    As = [*map(int, input().split())]

    # compute
    cost = 0
    for i, A in enumerate(As):
        if i%2 == 0:
            cost += A
        else:
            cost += A - 1

    # output
    if cost <= X:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
