import heapq

def main():
    # input
    Q = int(input())
    PXs = [[*map(int, input().split())] for _ in range(Q)]

    # compute
    bags = []
    heapq.heapify(bags)
    bsum = 0
    for PX in PXs:
        if PX[0] == 1:
            heapq.heappush(bags, PX[1]-bsum)
        elif PX[0] == 2:
            bsum += PX[1]
        else:
            print(heapq.heappop(bags) + bsum)

    # output


if __name__ == '__main__':
    main()
