def main():
  # input
  N, M = map(int, input().split())
  ABs = [list(map(int, input().split())) for _ in range(N)]

  # compute
  ABs.sort(key=lambda x: x[0])
  money = 0
  for a, b in ABs:
    if b < M:
      money += a*b
      M -= b
    else:
      money += a*M
      break

  # output
  print(money)


if __name__ == '__main__':
  main()
