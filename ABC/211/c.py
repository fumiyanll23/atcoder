from collections import defaultdict

def main():
    # input
    S = input()

    # compute
    ddict = defaultdict(int)
    for s in S:
        ddict[s] += 1

    # output
    if ddict['c'] and ddict['h'] and ddict['o'] and ddict['k'] and ddict['u'] and ddict['d'] and ddict['a'] and ddict['i']:
        print('OK')
    else:
        print(0)


if __name__ == '__main__':
    main()
