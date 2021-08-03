import heapq

def main():
    # input
    Q = int(input())
    PXs = [[*map(int, input().split())] for _ in range(Q)]

    # compute
    bags = []
    heapq.heapify(bags)
    badd = 0
    for PX in PXs:
        if PX[0] == 1:
            _, X = PX
            heapq.heappush(bags, X)
        elif PX[0] == 2:
            _, X = PX
            for i in range(len(bags)):
                bags[i] += X
        else:
            print(heapq.heappop(bags))

    # output


if __name__ == '__main__':
    main()
