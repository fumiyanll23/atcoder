def main():
    # input
    N = int(input())
    S = input()

    # compute
    x, ans = 0, 0
    for s in S:
        if s == 'I':
            x += 1
        else:
            x -= 1
        ans = max(ans, x)

    # output
    print(ans)


if __name__ == '__main__':
    main()
