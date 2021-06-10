def main():
    # input
    ABCs = [*map(int, input().split())]

    # compute
    ans = 0
    for i in range(3):
        ans += ABCs[i-1] * ABCs[i]

    # output
    print(2*ans)


if __name__ == '__main__':
    main()
