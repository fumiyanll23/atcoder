def main():
    # input
    S = input()

    # compute
    flag = False
    N =len(S)
    for i in range(N):
        for j in range(i,N):
            if S[:i]+S[j:] == 'keyence':
                flag = True

    # output
    if flag:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
