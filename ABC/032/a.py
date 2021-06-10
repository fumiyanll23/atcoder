def main():
    # input
    a = int(input())
    b = int(input())
    n = int(input())

    # compute

    # output
    ans = n
    while True:
        if ans%a==0 and ans%b==0:
            print(ans)
            exit()
        ans += 1


if __name__ == '__main__':
    main()
