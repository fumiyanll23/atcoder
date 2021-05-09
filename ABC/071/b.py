def main():
    # input
    S = input()

    # compute
    cnts = [0] * 26
    for s in S:
        cnts[ord(s)-97] += 1

    # output
    if cnts.count(0) != 0:
        print(chr(cnts.index(0)+97))
    else:
        print('None')


if __name__ == '__main__':
    main()
