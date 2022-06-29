def main():
    # input
    ABCs = [int(input()) for _ in range(3)]

    # compute

    # output
    for ABC in ABCs:
        print(sorted(ABCs, reverse=True).index(ABC) + 1)


if __name__ == '__main__':
    main()
