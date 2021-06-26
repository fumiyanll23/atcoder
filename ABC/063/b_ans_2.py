from collections import defaultdict

def main():
    # input
    S = input()

    # compute
    ddict = defaultdict(int)
    for s in S:
        ddict[s] += 1
    flag = True
    for key in ddict:
        if ddict[key] > 1:
            flag = False

    # output
    if flag:
        print('yes')
    else:
        print('no')


if __name__ == '__main__':
    main()
