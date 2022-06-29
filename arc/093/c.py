def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    As.insert(0, 0)
    As.append(0)
    all_sum = 0
    for i in range(N+1):
        all_sum += abs(As[i]-As[i+1])
    for i in range(N):
        print(all_sum - abs(As[i]-As[i+1]) - abs(As[i+1]-As[i+2]) + abs(As[i]-As[i+2]))

    # output


if __name__ == '__main__':
    main()
