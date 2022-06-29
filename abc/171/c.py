from math import log

def main():
    # input
    N = int(input())
    ALPHABET = 26

    # compute
    dig = int(log(N, ALPHABET)) + 1
    ans = []
    for _ in range(dig):
        ans.append(chr(96+N%ALPHABET))
        N //= ALPHABET

    # output
    print(''.join(reversed(ans)))


if __name__ == '__main__':
  main()
