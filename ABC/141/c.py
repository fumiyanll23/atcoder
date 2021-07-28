def main():
    # input
    N, K, Q = map(int, input().split())
    As = [int(input()) for _ in range(Q)]

    # compute
    points = [0] * N
    for A in As:
        points[A-1] += 1

    # output
    for point in points:
        if K > Q-point:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
