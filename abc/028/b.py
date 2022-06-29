def main():
    # input
    S = input()

    # compute
    anss = [0] * 6
    for s in S:
        if s == 'A':
            anss[0] += 1
        elif s == 'B':
            anss[1] += 1
        elif s == 'C':
            anss[2] += 1
        elif s == 'D':
            anss[3] += 1
        elif s == 'E':
            anss[4] += 1
        else:
            anss[5] += 1

    # output
    print(*anss)


if __name__ == '__main__':
    main()
