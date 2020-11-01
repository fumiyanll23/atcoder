def main():
  N = int(input())
  num = [list(map(int, input().split())) for _ in range(N)]

  ans = 0
  for i in range(N):
    n = num[i][1]-num[i][0]+1
    ans += n*(2*num[i][0]+n-1)//2
  print(ans)
if __name__ == "__main__":
    main()
