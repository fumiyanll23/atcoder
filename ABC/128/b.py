def main():
  # input
  N = int(input())
  SPs = [list(input().split()) for _ in range(N)]
  for i in range(N):
    SPs[i][1] = (-1) * int(SPs[i][1])

  # compute
  SPs_sorted = sorted(SPs, key=lambda x: (x[0], x[1]))
  for i in range(N):
    SPs_sorted[i][1] = str((-1)*SPs_sorted[i][1])
  name_and_number = []
  for i in range(N):
    name_and_number.append([SPs_sorted[i][0], SPs_sorted[i][1], i])

  # output
  for name,points in SPs:
    for i in range(N):
      if name==name_and_number[i][0] and points==name_and_number[i][1]:
        print(name_and_number[i][2]+1)


if __name__ == '__main__':
  main()
