def main():
  N, Y = map(int, input().split())

  for i in range(N+1):
    for j in range(N+1):
      for k in range(N+1):
        if 1000*i+5000*j+10000*k > Y:
          break
        elif 1000*i+5000*j+10000*k == Y and i+j+k == N:
          print(k, j, i)
          exit()
  print(-1, -1, -1)

if __name__ == "__main__":
    main()
