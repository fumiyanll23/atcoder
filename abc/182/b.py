def main():
  N = int(input())
  A = list(map(int, input().split()))

  cnt = [0 for _ in range(max(A))]
  for i in range(N):
    for div in range(2, max(A)+1):
      if A[i]%div == 0:
        cnt[div-1] += 1
  print(cnt.index(max(cnt)) + 1)

if __name__ == "__main__":
    main()
