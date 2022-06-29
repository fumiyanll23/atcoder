def main():
    # input
    O = input()
    E = input()

    # compute
    ans = ''
    for i in range(len(O)+len(E)):
        if i%2 == 0:
            ans += O[i//2]
        else:
            ans += E[i//2]

    # output
    print(ans)


if __name__ == '__main__':
    main()
