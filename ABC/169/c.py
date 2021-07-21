def main():
    # input
    A, B = input().split()
    A = int(A)
    B = int(B.replace('.', ''))

    # compute

    # output
    print(A * B // 100)

if __name__ == '__main__':
    main()
