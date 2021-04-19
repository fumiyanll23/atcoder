def main():
  # input
  N = int(input())
  Hs = list(map(int, input().split()))

  # compute
  for i in range(N-1):
    if Hs[i] > min(Hs[i:]):
      Hs[i] -= 1
  flag = True
  for i in range(N-1):
    if Hs[i] > Hs[i+1]:
      flag = False

  # output
  if flag:
    print('Yes')
  else:
    print('No')


if __name__ == '__main__':
  main()
