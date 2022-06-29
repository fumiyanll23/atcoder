# ABC197C - ORXOR

def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    tmps, anss = [], []
    # compute variable 'comb'
    for i in range(comb):
        tmps.append(As[i] | As[i])

    # output
    print(min(anss))

if __name__ == '__main__':
    main()
