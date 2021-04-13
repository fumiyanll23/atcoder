def main():
    # input
    N = int(input())
    Ass = []
    for _ in range(2):
        Ass.append(list(map(int, input().split())))

    # compute
    candies = [0 for _ in range(N)]
    for i in range(N):
        candies[i] += sum(Ass[0][:i+1]) + sum(Ass[1][i:])

    # output
    print(max(candies))


if __name__ == '__main__':
    main()
