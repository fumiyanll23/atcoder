### As you know, I recieved TLE ...... :(

def main():
  # input
  N, W = map(int, input().split())
  STP = [list(map(int, input().split())) for _ in range(N)]

  # compute
  stop = 0
  for i in range(N):
    if stop < STP[i][1]:
      stop = STP[i][1]
  total = [0 for _ in range(stop)]
  for i in range(N):
    for j in range(stop):
      if STP[i][0] <= j < STP[i][1]:
        total[j] += STP[i][2]
  total.sort(reverse=True)

  # output
  for i in range(len(total)):
    if total[i] > W:
      print('No')
      exit()
  print('Yes')

if __name__ == "__main__":
    main()
