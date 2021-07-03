from itertools import combinations

def main():
    # input
    N, P, Q = map(int, input().split())
    As = [*map(int, input().split())]

    # compute
    ans = 0
    for subAs in combinations(As, 5):
        tmp_prd = 1
        for subA in subAs:
            tmp_prd = tmp_prd * subA % P
        if tmp_prd == Q:
            ans += 1

    # output
    print(ans)


if __name__ == '__main__':
    main()
