def main():
  N = int(input())
  dot = [list(map(int, input().split())) for _ in range(N)]

  dot.sort()
  for i in range(N):
    for j in range(i+1, N):
      for k in range(j+1, N):
        dx1 = dot[j][0] - dot[i][0]
        dx2 = dot[k][0] - dot[j][0]
        dy1 = dot[j][1] - dot[i][1]
        dy2 = dot[k][1] - dot[j][1]
        if dx2*dy1 == dx1*dy2:
          print('Yes')
          exit()
  print('No')

if __name__ == "__main__":
    main()
