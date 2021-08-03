def main():
    # input
    X = input()

    # compute
    flag = True
    if X[0] == X[1] == X[2] == X[3]:
        flag = False
    cnt = 0
    for i in range(3):
        if (int(X[i])+1)%10 == int(X[i+1]):
            cnt += 1
    if cnt == 3:
        flag = False

    # output
    if flag:
        print('Strong')
    else:
        print('Weak')


if __name__ == '__main__':
    main()
