def main():
    # input
    S = input()

    # compute
    ans, cnt = 0, 0
    for s in S[::-1]:
        if s == 'W':
            cnt += 1
        else:
            ans += cnt

    # output
    print(ans)


if __name__ == '__main__':
    main()
