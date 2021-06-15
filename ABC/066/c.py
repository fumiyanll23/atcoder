from collections import deque

def main():
    # input
    n = int(input())
    As = [*map(int, input().split())]

    # compute
    Bs = deque()
    rev = False
    for A in As:
        if rev:
            Bs.appendleft(A)
        else:
            Bs.append(A)
        rev = not rev
    if rev:
        Bs.reverse()

    # output
    print(*Bs)


if __name__ == '__main__':
    main()
