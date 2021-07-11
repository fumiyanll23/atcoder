def main():
    # input
    N, K = input().split()
    K = int(K)
    # compute
    for cnt in range(K):
        ten = 0
        for i, n in enumerate(N):
            ten += int(n) * 8**(len(N)-1-i)
        nine = ''
        for i in reversed(range(21)):
            if ten > 9**i:
                tmp_digit = ten // (9**i)
                nine += str(tmp_digit)
                ten -= tmp_digit * 9**i
            if ten <= 0:
                break
        N = nine.replace('8', '5')
    # output
    print(int(N))
if __name__ == '__main__':
    main()
