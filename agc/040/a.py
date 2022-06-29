def main():
    # input
    S = input()

    # compute
    N = len(S) + 1
    ans = []
    cnt = 0

    for i in range(N-2):
        if S[i] == '<':
            ans.append(cnt)
            print(i, cnt)
            if S[i+1] == '<':
                cnt += 1
                print(i, '+1')
        else:
            ans.append('>')
            print(i, '>')
    if S[-2] == S[-1] == '<':
        ans.append(cnt)
        print(N-2, cnt)
    elif S[-1] == '<':
        ans.append(1)
        print(N-2, 1)
    else:
        ans.append(0)
        print(N-2, 0)

    cnt = 0
    print()
    if S[-1] == '>':
        ans.append(0)
        print(N-1, 0)
    else:
        ans.append('<')
        print(N-1, '<')
    for i in reversed(range(1,N-1)):
        if ans[i] == '>':
            ans[i] = cnt
            print(i, cnt)
            if ans[i-1] == '>':
                cnt += 1
                print(i, '+1')
        else:
            print(i)

    # output
    print(len(ans), ';', ans)
    # print(sum(ans))


if __name__ == '__main__':
    main()
