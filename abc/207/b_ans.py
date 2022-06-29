def main():
    # input
    A, B, C, D = map(int, input().split())

    # compute
    ans = -1
    diff = C*D - B
    if diff > 0:
        ans = (A+diff-1) // diff

    # output
    print(ans)


if __name__ == '__main__':
    main()
