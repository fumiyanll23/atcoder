def main():
    # input
    N, L = map(int, input().split())

    # compute
    apples = [*range(L, L+N)]

    # output
    if 0 < L < L+N-1:
        print(sum(apples) - apples[0])
    elif L < L+N-1 < 0:
        print(sum(apples) - apples[-1])
    else:
        print(sum(apples))


if __name__ == '__main__':
    main()
