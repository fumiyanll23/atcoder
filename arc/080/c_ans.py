def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    odd = sum([A%2 != 0 for A in As])
    double_even = sum([A%4 == 0 for A in As])
    even = N - odd - double_even

    # output
    if even == 0:
        if odd <= double_even+1:
            print('Yes')
        else:
            print('No')
    else:
        if odd <= double_even:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
