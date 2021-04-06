def main():
    # input
    s = input()

    # compute
    ans = ''
    n = len(s)
    for i in range(n):
        if i%2 == 0:
            ans += s[i]

    # output
    print(ans)

if __name__ == '__main__':
    main()
