def main():
    # input
    A, B, C, X, Y = map(int, input().split())

    # compute
    if X > Y:
        r = A * (X-Y)
    elif Y > X:
        r = B * (Y-X)
    else:
        r = 0
    cost = (A+B)*min(X, Y) + r
    cost_min = C*2*min(X, Y) + r
    cost_max = C*2*max(X, Y)

    # output
    print(min(cost, min(cost_min, cost_max)))


if __name__ == '__main__':
    main()
