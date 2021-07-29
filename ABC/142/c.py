def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    studentss = []
    for i, A in enumerate(As):
        studentss.append([A, i])
    anss = []
    for _, num in sorted(studentss):
        anss.append(num + 1)

    # output
    print(*anss)


if __name__ == '__main__':
    main()
