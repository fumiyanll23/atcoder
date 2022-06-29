from math import pow

def main():
    # input
    N = int(input())

    # compute
    LOOP = 10**2
    for i in range(1,LOOP):
        for j in range(1,LOOP):
            if 3**i+5**j == N:
                print(i, j)
                exit()

    # output
    print(-1)


if __name__ == '__main__':
    main()
