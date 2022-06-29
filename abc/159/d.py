def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    cnts = [0] * N
    for A in As:
        cnts[A-1] += 1
    combs = []
    for cnt in cnts:
        if cnt > 1:
            combs.append(cnt * (cnt-1) // 2)
        else:
            combs.append(0)
    ans = sum(combs)
    for A in As:
        print(ans + (cnts[A-1]-1)*(cnts[A-1]-2)//2 - combs[A-1])

    # output


if __name__ == '__main__':
    main()
