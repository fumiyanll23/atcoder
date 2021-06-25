def main():
    # input
    N = int(input())
    S = input()

    # compute
    x = 0
    ans = 0
    for s in S:
        if s == 'I':
            x += 1
            if ans < x:
                ans = x
        else:
            x -= 1

    # output
    print(ans)


if __name__ == '__main__':
    main()
