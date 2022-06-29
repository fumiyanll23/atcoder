def main():
  N = int(input())
  A = list(map(int, input().split()))

  tmpsum = [0 for _ in range(N)]
  for i in range(N):
    for j in range(i+1):
      tmpsum[i] += A[j]
  ans = 0
  for i in range(N):
    if tmpsum[i] > 0:
      ans += tmpsum[i]
  for i in range(N):
    if A[i] > 0:
      ans += A[i]
    else:
      break
  print(ans)

if __name__ == "__main__":
    main()
