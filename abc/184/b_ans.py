def main():
    # input
    N, X = map(int, input().split())
    S = input()

    # compute
    for s in S:
        if s == 'o':
            X += 1
        elif X:
            X -= 1

    # output
    print(X)


if __name__ == '__main__':
    main()
