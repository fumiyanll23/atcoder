def main():
    # input
    N = int(input())

    # compute
    cnt = 1
    while True:
        if (cnt+1)*cnt//2 >= N:
            break
        else:
            cnt += 1

    # output
    print(cnt)


if __name__ == '__main__':
    main()
