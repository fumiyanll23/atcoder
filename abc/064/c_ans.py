def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    colors = set()
    cnt = 0
    for A in As:
        if A < 3200:
            colors.add(A//400)
        else:
            cnt += 1

    # output
    print(max(1, len(colors)), len(colors)+cnt)


if __name__ == '__main__':
    main()
