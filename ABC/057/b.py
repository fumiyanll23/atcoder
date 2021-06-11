def main():
    # input
    N, M = map(int, input().split())
    ABs = [[*map(int, input().split())] for _ in range(N)]
    CDs = [[*map(int, input().split())] for _ in range(M)]

    # compute
    for A,B in ABs:
        distance = float('inf')
        checkpoint = 0
        for i,CD in enumerate(CDs):
            if distance > abs(A-CD[0])+abs(B-CD[1]):
                distance = abs(A-CD[0])+abs(B-CD[1])
                checkpoint = i + 1
        print(checkpoint)

    # output


if __name__ == '__main__':
    main()
