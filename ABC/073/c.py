def main():
    # input
    N = int(input())
    As = [int(input()) for _ in range(N)]

    # compute
    ans_set = set()
    for a in As:
        if a in ans_set:
            ans_set.discard(a)
        else:
            ans_set.add(a)

    # output
    print(len(ans_set))


if __name__ == '__main__':
    main()
