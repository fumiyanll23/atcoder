def main():
    # input
    S = input()

    # compute
    N = len(S)
    cnt, ans = 0, 0
    for i,s in enumerate(S):
        if s == 'B':
            cnt += 1
            ans += N - cnt - i

    # output
    print(ans)


if __name__ == '__main__':
    main()
