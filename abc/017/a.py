def main():
    # input
    ses = [[*map(int, input().split())] for _ in range(3)]

    # compute
    ans = 0
    for s,e in ses:
        ans += s*e / 10

    # output
    print(int(ans))


if __name__ == '__main__':
    main()
