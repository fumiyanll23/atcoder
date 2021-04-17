def main():
    # input
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))

    # compute
    numbers = [0] * (10**3+5)
    for i in As:
        numbers[i] += 1
    for i in Bs:
        numbers[i] += 1
    anss = []
    for i, figure in enumerate(numbers):
        if figure == 1:
            anss.append(i)

    # output
    print(*anss)

if __name__ == '__main__':
    main()
