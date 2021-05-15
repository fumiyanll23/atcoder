from math import factorial

def permutation(n: int, r: int) -> int:
    return factorial(n) // factorial(n-r)

def main():
    # input
    S = input()

    # compute
    o, q = 0, 0
    for s in S:
        if s == 'o':
            o += 1
        elif s == '?':
            q += 1
    ans = 0
    if o == 4:
        ans += o*permutation(4,4)
    if o>=3 and q>=1:
        ans += o*permutation(4,3) * q*permutation(1,1)
    if o>=2 and q>=2:
        ans += o*permutation(4,2) * permutation(2,2)
    if o>=1 and q>=3:
        ans += o*permutation(4,1) * permutation(3,3)
    if o==0 and q>=4:
        ans += o*permutation(4,4)

    # output
    if o > 4:
        print(0)
    else:
        print(ans)


if __name__ == '__main__':
    main()
