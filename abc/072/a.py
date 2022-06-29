def main():
    # input
    X, t = map(int, input().split())

    # compute

    # output
    if X < t:
        print(0)
    else:
        print(X-t)

if __name__ == '__main__':
    main()
