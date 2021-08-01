def main():
  # input
  N = int(input())
  As = [*map(int, input().split())]

  # compute
  cnts = [0] * N
  for A in As:
    cnts[A-1] += 1

  # output
  for cnt in cnts:
    print(cnt)


if __name__ == '__main__':
  main()
