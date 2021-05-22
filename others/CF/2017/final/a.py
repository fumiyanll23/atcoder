def main():
    # input
    S = input()

    # compute
    cnt = S.count('A')

    # output
    if cnt == 0:
        if S == 'KIHBR':
            print('YES')
        else:
            print('NO')
    elif cnt == 1:
        if S=='AKIHBR' or S=='KIHABR' or S=='KIHBAR' or S=='KIHBRA':
            print('YES')
        else:
            print('NO')
    elif cnt == 2:
        if S=='AKIHABR' or S=='AKIHBAR' or S=='AKIHBRA':
            print('YES')
        elif S=='KIHABAR' or S=='KIHABRA':
            print('YES')
        elif S=='KIHBARA':
            print('YES')
        else:
            print('NO')
    elif cnt == 3:
        if S=='AKIHABAR' or S=='AKIHABRA' or S=='AKIHBARA':
            print('YES')
        elif S == 'KIHABARA':
            print('YES')
        else:
            print('NO')
    elif cnt == 4:
        if S == 'AKIHABARA':
            print('YES')
        else:
            print('NO')
    else:
        print('NO')


if __name__ == '__main__':
    main()
