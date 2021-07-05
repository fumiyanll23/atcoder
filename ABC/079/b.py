from math import sqrt

def lucas(n: int) -> int:
  return round(pow((1+sqrt(5))/2, n) + pow((1-sqrt(5))/2, n))


def main():
  # input
  N = int(input())

  # compute

  # output
  print(lucas(N))


if __name__ == '__main__':
  main()
