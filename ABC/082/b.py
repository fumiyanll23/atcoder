def main():
    # input
    s = [*input()]
    t = [*input()]

    # compute
    slen, tlen = len(s), len(t)
    s_dash = [0] * slen
    t_dash = [0] * tlen
    for i in range(slen):
        s_dash[i] = int(ord(s[i]))
    for i in range(tlen):
        t_dash[i] = int(ord(t[i]))

    # output
    if sorted(s_dash) < reversed(sorted(t_dash)):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
