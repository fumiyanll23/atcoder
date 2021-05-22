def main():
    # input
    S = list(input())

    # compute
    for i,s in enumerate(S):
        if s == '6':
            S[i] = '9'
        elif s == '9':
            S[i] = '6'

    # output
    print(''.join(reversed(S)))


if __name__ == '__main__':
    main()
