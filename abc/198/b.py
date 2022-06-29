def main():
    # input
    N = str(input())

    # compute
    i, cnt, flag = 0, 0, True
    if N == '0':
        print('Yes')
        exit()
    while N[-(i+1)] == '0':
        cnt += 1
        i += 1
    if cnt == 0:
        for i in range(len(N)//2):
            if N[i] != N[-(i+1)]:
                flag = False
    else:
        for i in range((len(N)-cnt)//2):
            if N[i] != N[-(cnt+i+1)]:
                flag = False

    # output
    if flag:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
