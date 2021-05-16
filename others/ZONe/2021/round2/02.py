from math import sqrt

def is_prime(n: int) -> bool:
    '''
    judge while n is a prime number or not
    - n: natural number
    '''
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False

    return True


def generate_prime_numbers(n: int, m: int) -> list:
    '''
    generate prime numbers list from n to m
    - n, m: natural number (n <= m)
    '''
    primes = []
    for i in range(n, m):
        if is_prime(i):
            primes.append(i)

    return primes


def main():
    # input
    N = 20
    xss = [list(map(int, input().split())) for _ in range(N)]

    # compute
    cnt = 0
    primes = generate_prime_numbers(1, 1000)
    for i in range(N):
        for j in range(N):
            if xss[i][j] in primes:
                cnt += 1

    # output
    print(cnt)


if __name__ == '__main__':
    main()
