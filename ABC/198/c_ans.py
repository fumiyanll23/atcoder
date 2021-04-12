import math

def main():
    # input
    R, X, Y = map(int, input().split())

    # compute
    d = math.sqrt(X**2+Y**2)

    # output
    if d == R:
        print(1)
    elif d <= 2*R:
        print(2)
    else:
        print(math.ceil(d/R))

if __name__ == '__main__':
    main()
