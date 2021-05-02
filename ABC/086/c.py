def main():
  # input
  N = int(input())
  txys = [list(map(int, input().split())) for _ in range(N)]

  # compute
  flag = True
  t, x, y = 0, 0, 0
  for i in range(N):
    dt, dx, dy = txys[i][0]-t, abs(txys[i][1]-x), abs(txys[i][2]-y)
    if dt == dx+dy:
      pass
    elif dt>(dx+dy) and dt%2==(dx+dy)%2:
      pass
    else:
      flag = False
    t, x, y = txys[i]

  # output
  if flag:
    print('Yes')
  else:
    print('No')


if __name__ == '__main__':
  main()
