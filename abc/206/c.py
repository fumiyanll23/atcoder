from collections import defaultdict

def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    dict = defaultdict(int)
    for A in As:
        dict[A] += 1
    ans = N*(N-1)//2
    for d in dict:
        ans -= dict[d]*(dict[d]-1)//2

    # output
    print(ans)


if __name__ == '__main__':
    main()
