def main():
  N = int(input())
  # A[*][0]: time, A[*][1]: x coordinate, A[*][2]: y coordinate
  A = [list(map(int, input().split())) for _ in range(N)]

  flag = False
  for i in range(N-1):
    tdiff = A[i+1][0] - A[i][0]
    xdiff = abs(A[i+1][1] - A[i][1])
    ydiff = abs(A[i+1][2] - A[i][2])
    if tdiff == xdiff+ydiff:
      flag = True
    elif (xdiff+ydiff-tdiff)%2 == 0:
      flag = True
  if flag:
    print('Yes')
  else:
    print('No')

if __name__ == "__main__":
    main()
