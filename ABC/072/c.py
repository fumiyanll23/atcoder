def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    As.sort()
    cnts = [0] * (10**5+3)
    for a in As:
        cnts[a-1] += 1
        cnts[a] += 1
        cnts[a+1] += 1

    # output
    print(max(cnts))


if __name__ == '__main__':
    main()
