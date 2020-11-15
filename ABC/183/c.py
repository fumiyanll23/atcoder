### It will be desolved by deque but I do NOT know how to use deque !!!!!
#from collections import deque

def main():
  # input
  N, K = map(int, input().split())
  T = [list(map(int, input().split())) for _ in range(N)]

  # compute
  cnt = 0
  for i in range(N):
    time = T[0][i]
    for j in range(1, N):
      time += T[i][j]
      print(time)
    if time == K:
      cnt += 1

  # output
  print(cnt)


if __name__ == "__main__":
    main()
