def main():
    # input
    s = input()

    # compute
    ans = []
    for S in s:
        if S == '0':
            ans.append('0')
        elif S == '1':
            ans.append('1')
        else:
            if ans == []:
                pass
            else:
                ans.pop(-1)

    # output
    print(''.join(ans))


if __name__ == '__main__':
    main()
