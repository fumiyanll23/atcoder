from itertools import permutations

def main():
    # input
    N = int(input())
    Ps = tuple(map(int, input().split()))
    Qs = tuple(map(int, input().split()))

    # compute
    for i,r in enumerate(permutations(range(1,N+1),N)):
        if r == Ps:
            a = i
        if r == Qs:
            b = i

    # output
    print(abs(a-b))


if __name__ == '__main__':
    main()
