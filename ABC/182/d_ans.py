def main():
  # input
  N = int(input())
  A = list(map(int, input().split()))

  # compute
  p = [0 for _ in range(N)]
  q = [0 for _ in range(N)]
  ## compute partial sums
  for i in range(N):
    if i == 0:
      p[i] = A[i]
      q[i] = max(0, A[i])
    else:
      p[i] = p[i-1] + A[i]
      q[i] = max(q[i-1], p[i])
  ans, now = 0, 0
  for i in range(N):
    ans = max(ans, now+q[i])
    now += p[i]

  # output
  print(ans)

if __name__ == "__main__":
    main()
