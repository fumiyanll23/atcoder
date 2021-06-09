def main():
    # input
    A = int(input())

    # compute
    ans = 0
    for i in range(A):
        for j in range(i+1):
            if i+j==A and ans<i*j:
                ans = i*j

    # output
    print(ans)


if __name__ == '__main__':
    main()
