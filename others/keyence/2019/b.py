def main():
    # input
    S = input()

    # compute
    flag = False
    T = 'keyence'
    for i in range(len(T)):
        if T[:i] in S and T[i:] in S:
            print(T[:i], T[i:])
            flag = True

    # output
    if flag:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
