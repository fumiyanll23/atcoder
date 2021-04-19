def main():
    # input
    N = int(input())
    Hs = list(map(int, input().split()))

    # compute
    flag = True
    for i in reversed(range(N-1)):
        if Hs[i]-Hs[i+1] == 1:
            Hs[i] -= 1
    for i in range(N-1):
        if Hs[i] > Hs[i+1]:
            flag = False

    # output
    if flag:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
