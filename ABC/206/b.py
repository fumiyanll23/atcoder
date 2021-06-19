def main():
    # input
    N = int(input())

    # compute
    cnt = 0
    while (cnt+1)*cnt//2 < N:
        cnt += 1

    # output
    print(cnt)


if __name__ == '__main__':
    main()
