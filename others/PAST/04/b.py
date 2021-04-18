from math import floor

def main():
    # input
    X, Y = map(int, input().split())

    # compute

    # output
    if Y == 0:
        print('ERROR')
    elif X%Y == 0:
        print(''.join(str(X//Y)+'.00'))
    elif len(str(X/Y)) == 3:
        print(''.join(str(X/Y)+'0'))
    else:
        ans = floor(X*(10**2)/Y)/(10**2)
        print(ans)


if __name__ == '__main__':
    main()
