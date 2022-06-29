def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    cnts = [0] * 200
    for a in As:
        cnts[a%200] += 1
    ans = 0
    for cnt in cnts:
        ans += cnt*(cnt-1)//2

    # output
    print(ans)


if __name__ == '__main__':
    main()
