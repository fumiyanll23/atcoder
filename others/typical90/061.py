from collections import deque

def main():
    # input
    Q = int(input())
    txs = [[*map(int, input().split())] for _ in range(Q)]

    # compute
    deq = deque()

    # output
    for tx in txs:
        t, x = tx
        if t == 1:
            deq.appendleft(x)
        elif t == 2:
            deq.append(x)
        else:
            print(deq[x-1])


if __name__ == '__main__':
    main()
