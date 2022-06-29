def main():
    # input
    N = int(input())

    # compute

    # output
    if N <= 59:
        print('Bad')
    elif N <= 89:
        print('Good')
    elif N <= 99:
        print('Great')
    else:
        print('Perfect')


if __name__ == '__main__':
    main()
