def main():
    # input
    N, A, B = map(int, input().split())
    S = input()

    # compute
    passed, foreign = 0, 0

    # output
    for i in range(N):
        if S[i]=='a':
            if passed < A+B:
                print('Yes')
                passed += 1
            else:
                print('No')
        elif S[i] == 'b':
            foreign += 1
            if passed<A+B and foreign<=B:
                print('Yes')
                passed += 1
            else:
                print('No')
        else:
            print('No')


if __name__ == '__main__':
    main()
