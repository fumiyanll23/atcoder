def main():
    # input
    S = list(input())

    # compute
    N = len(S)
    cnt = 0
    while ''.join(S).count('BW') != 0:
        for i in range(N-1):
            if S[i]=='B' and S[i+1]=='W':
                S[i], S[i+1] = S[i+1], S[i]
                cnt += 1
                print(cnt, ''.join(S))

    # output
    print(cnt)


if __name__ == '__main__':
    main()
