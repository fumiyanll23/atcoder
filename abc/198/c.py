import math

def main():
    # input
    R, X, Y = map(int, input().split())

    # compute
    d = math.sqrt(X**2+Y**2)

    # output
    if d//R == 0:
        print(2)
    elif d%R == 0:
        print(int(d // R))
    else:
        print(int(d//R) + 1)

if __name__ == '__main__':
    main()
