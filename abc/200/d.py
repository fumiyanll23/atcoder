def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    Bs, Cs = As, As
    Bs_index, Cs_index = list(range(1,N)), list(range(1,N+1))
    for _ in range(2*N):
        if abs(sum(Bs)-sum(Cs))%200 == 0:
            break
        else:
            if len(Bs) < len(Cs):
                Cs.remove(As.index(max(As)))
            else:
                Bs.remove(As.index(max(As)))
    x, y = len(Bs), len(Cs)

    ## check while Bs==Cs or not
    flag = False
    if x != y:
        flag = True
    else:
        for i in range(x):
            if Bs[i] == Cs[i]:
                flag = True

    # output
    if flag:
        print('Yes')
        print(x, *Bs)
        print(y, *Cs)
    else:
        print('No')


if __name__ == '__main__':
    main()
