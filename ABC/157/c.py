def main():
    # input
    N, M = map(int, input().split())
    scs = [list(map(int, input().split())) for _ in range(M)]

    # compute
    if N == 1:
        numbers = range(0, 10)
    elif N == 2:
        numbers = range(10, 100)
    else:
        numbers = range(100, 1000)
    for i in numbers:
        flag = True
        number = list(map(int, str(i)))
        for s,c in scs:
            if number[s-1] == c:
                pass
            else:
                flag = False
        if flag:
            print(''.join(list(map(str, number))))
            exit()
        else:
            pass

    # output
    print(-1)


if __name__ == '__main__':
  main()
