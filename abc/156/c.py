def main():
  # input
  N = int(input())
  Xs = [*map(int, input().split())]

  # compute
  ans = float('inf')
  for p in range(min(Xs), max(Xs)+1):
    dist = 0
    for X in Xs:
      dist += (X - p)**2
    ans = min(ans, dist)

  # output
  print(ans)


if __name__ == '__main__':
  main()
