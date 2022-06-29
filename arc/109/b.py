def binary_search(key: int) -> int:
    ng = key
    ok = 0
    nsum = (key+1)*key // 2
    n1sum = nsum + key + 1
    while abs(ok-ng) > 1:
        middle = (ok+ng) // 2
        if  n1sum-middle*(middle-1)//2 >= nsum:
            ok = middle
        else:
            ng = middle

    return ok


def main():
    # input
    n = int(input())

    # compute

    # output
    if n==1 or n==2:
        print(1)
    elif n == 3:
        print(2)
    else:
        print(n - binary_search(n) + 2)


if __name__ == '__main__':
    main()
