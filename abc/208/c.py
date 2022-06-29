def main():
    # input
    N, K = map(int, input().split())
    Ass = [*map(int, input().split())]

    # compute
    for i, A in enumerate(Ass):
        Ass[i] = [i, A]
    Ass.sort(key=lambda x: x[1])
    least = K // N
    for As in Ass:
        As[1] = least
    K -= least * N
    for i in range(K):
        Ass[i][1] += 1
    Ass.sort(key=lambda x: x[0])

    # output
    for As in Ass:
        print(As[1])


if __name__ == '__main__':
    main()
