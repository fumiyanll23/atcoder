def main():
    # input
    Ss = [input() for _ in range(12)]

    # compute
    ans = 0
    for S in Ss:
        if 'r' in S:
            ans += 1

    # output
    print(ans)


if __name__ == '__main__':
    main()
