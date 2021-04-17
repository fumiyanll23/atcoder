from math import gcd

def main():
    # input
    A, B = map(int, input().split())

    # compute
    anss_A = [0] * 2*10**5
    anss_B = [0] * 2*10**5
    for i in range(A+1, B+1):
        anss_A[i-A-1] = gcd(A, i)
    for i in range(A, B):
        anss_B[i-A] = gcd(B, i)

    # output
    print(max(max(anss_A), max(anss_B)))

if __name__ == '__main__':
    main()
