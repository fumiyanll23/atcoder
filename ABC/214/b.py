def main():
    # input
    S, T = map(int, input().split())

    # compute
    ans = 0
    for a in range(101):
        for b in range(101):
            for c in range(101):
                if a+b+c <= S and a*b*c <= T:
                    ans += 1

    # output
    print(ans)


if __name__ == '__main__':
    main()
