def main():
    # input
    A, B, C = map(int, input().split())

    # compute
    MODSS = [
        [0],
        [1],
        [2,4,8,6],
        [3,9,7,1],
        [4,6],
        [5],
        [6],
        [7,9,3,1],
        [8,4,2,6],
        [9,1]
    ]
    A %= 10
    BC = pow(B, C, len(MODSS[A]))

    # output
    print(MODSS[A][BC-1])

if __name__ == '__main__':
    main()
