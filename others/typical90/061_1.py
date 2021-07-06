def main():
    # input
    Q = int(input())
    txs = [[*map(int, input().split())] for _ in range(Q)]

    # compute
    decks = []
    for tx in txs:
        t, x = tx
        if t == 1:
            decks.insert(0, x)
        elif t == 2:
            decks.append(x)
        else:
            print(decks[x-1])

    # output


if __name__ == '__main__':
    main()
