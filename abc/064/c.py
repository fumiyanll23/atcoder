def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    ans = set()
    cnt = 0
    for A in As:
        if A < 400:
            ans.add(0)
        elif A < 800:
            ans.add(1)
        elif A < 1200:
            ans.add(2)
        elif A < 1600:
            ans.add(3)
        elif A < 2000:
            ans.add(4)
        elif A < 2400:
            ans.add(5)
        elif A < 2800:
            ans.add(6)
        elif A < 3200:
            ans.add(7)
        else:
            cnt += 1
    minimum = len(ans)

    # output
    if cnt == N:
        print(1, N)
    else:
        print(minimum, minimum+cnt)


if __name__ == '__main__':
    main()
