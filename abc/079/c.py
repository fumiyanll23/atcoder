def main():
    # input
    A, B, C, D = list(map(int, input()))

    # compute

    # output
    if A+B+C+D == 7:
        print(f'{A}+{B}+{C}+{D}=7')
    elif A-B+C+D == 7:
        print(f'{A}-{B}+{C}+{D}=7')
    elif A+B-C+D == 7:
        print(f'{A}+{B}-{C}+{D}=7')
    elif A+B+C-D == 7:
        print(f'{A}+{B}+{C}-{D}=7')
    elif A-B-C+D == 7:
        print(f'{A}-{B}-{C}+{D}=7')
    elif A+B-C-D == 7:
        print(f'{A}+{B}-{C}-{D}=7')
    elif A-B+C-D == 7:
        print(f'{A}-{B}+{C}-{D}=7')
    else:
        print(f'{A}-{B}-{C}-{D}=7')


if __name__ == '__main__':
    main()
