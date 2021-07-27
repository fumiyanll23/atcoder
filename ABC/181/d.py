from collections import defaultdict

def main():
    # input
    S = input()
    N = len(S)

    # compute
    flag = False
    if N == 1:
        if int(S)%8 == 0:
            flag = True
    elif N == 2:
        if int(S[0]+S[1])%8 == 0 or int(S[1]+S[0])%8 == 0:
            flag = True
    else:
        sddict = defaultdict(int)
        for s in S:
            sddict[s] += 1
        for i in range(13, 125):
            cddict = defaultdict(int)
            for c in str(8 * i):
                cddict[c] += 1
            if all([sddict[k] >= v for k, v in cddict.items()]):
                flag = True
                break

    # output
    if flag:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
