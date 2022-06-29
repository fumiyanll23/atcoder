def main():
    # input
    E = input()
    O = input()

    # compute
    ans = ''
    for i in range(len(E)):
        ans += E[i]
        if i < len(O):
            ans += O[i]

    # output
    print(ans)


if __name__ == '__main__':
    main()
