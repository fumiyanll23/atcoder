def main():
    # input
    ABCs = list(map(int, input().split()))

    # compute
    s = sum(ABCs)
    while not(s%3==0 and s//3>=max(ABCs)):
        s += 1

    # output
    print(s, sum(ABCs))
    print((s-sum(ABCs)) // 2)

if __name__ == '__main__':
    main()
