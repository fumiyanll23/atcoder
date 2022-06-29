from math import log

def main():
    # input
    N = int(input())

    # compute
    LOOP = 10**2
    for i in range(LOOP):
        if N-5**i < 0:
            break
        elif log(N-5**i, 3).is_integer():
            print(int(log(N-5**i, 3)), i)
            exit()

    # output
    print(-1)


if __name__ == '__main__':
    main()
