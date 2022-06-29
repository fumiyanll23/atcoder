from math import gcd
from functools import reduce

def my_gcd(*numbers: int) -> int:
  return reduce(gcd, numbers)

def main():
  # input
  N = int(input())
  As = list(map(int, input().split()))

  # compute

  # output
  if N == 1:
    print(As[0])
  else:
    print(my_gcd(*As))


if __name__ == '__main__':
  main()
