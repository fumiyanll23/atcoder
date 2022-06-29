from math import sqrt

def main():
    # input
    N = int(input())

    # compute
    ans = 0
    for i in range(1,int(sqrt(N))+1):
        if (N/i).is_integer():
            ans = max(len(str(i)), len(str(N//i)))

    # output
    print(ans)


if __name__ == '__main__':
    main()
