def main():
    # input
    A, B, C, X, Y = map(int, input().split())

    # compute
    AB = min(A+B, 2*C) * min(X, Y)

    # output
    if X > Y:
        print(AB + min(A, 2*C)*(X-Y))
    else:
        print(AB + min(B, 2*C)*(Y-X))


if __name__ == '__main__':
    main()
