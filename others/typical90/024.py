def main():
    # input
    N, K = map(int, input().split())
    As = [*map(int, input().split())]
    Bs = [*map(int, input().split())]

    # compute
    diff = 0
    for A, B in zip(As, Bs):
        diff += abs(A - B)

    # output
    if K>=diff and K%2==diff%2:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
