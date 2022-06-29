def binary_search(key: int) -> int:
    ng = key+1
    ok = 0
    while abs(ok-ng) > 1:
        middle = (ok+ng) // 2
        if  (middle+1)*middle//2 <= key+1:
            ok = middle
        else:
            ng = middle

    return ok


def main():
    # input
    n = int(input())

    # compute

    # output
    print(n - binary_search(n) + 1)


if __name__ == '__main__':
    main()
