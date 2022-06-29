def main():
    # input
    N = int(input())
    Xs = [*map(int, input().split())]

    # compute
    Xs_sort = sorted(Xs)
    med_r, med_l = Xs_sort[N//2-1], Xs_sort[N//2]
    for X in Xs:
        if X <= med_r:
            print(med_l)
        else:
            print(med_r)

    # output


if __name__ == '__main__':
    main()
