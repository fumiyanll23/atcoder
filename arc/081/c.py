from collections import defaultdict

def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    As.sort()
    ddict = defaultdict(int)
    for A in As:
        ddict[A] += 1
    recs = [0, 0]
    sqs = [0]
    for d in ddict:
        if ddict[d] >= 2:
            recs.append(d)
            if ddict[d] >= 4:
                sqs.append(d)

    # output
    print(max(recs[-1]*recs[-2], sqs[-1]*sqs[-1]))


if __name__ == '__main__':
    main()
