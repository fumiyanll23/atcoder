from math import sqrt

def main():
    # input
    N = int(input())

    # compute
    divs = []
    for i in range(1,int(sqrt(N))+1):
        if N%i == 0:
            divs.append(i+N//i-2)

    # output
    print(min(N-1, min(divs)))


if __name__ == '__main__':
    main()
