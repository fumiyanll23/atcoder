from math import pi

def main():
    # input
    N = int(input())
    Rs = [int(input()) for _ in range(N)]

    # compute
    ans = 0
    for i, R in enumerate(reversed(sorted(Rs))):
        if i%2 == 0:
            ans += R ** 2
        else:
            ans -= R ** 2

    # output
    print(ans * pi)


if __name__ == '__main__':
    main()
