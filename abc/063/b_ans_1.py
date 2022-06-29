def main():
    # input
    S = input()

    # compute
    flag = True
    for i in range(len(S)-1):
        for j in range(i+1,len(S)):
            if S[i] == S[j]:
                flag = False

    # output
    if flag:
        print('yes')
    else:
        print('no')


if __name__ == '__main__':
    main()
