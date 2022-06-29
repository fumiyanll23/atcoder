def main():
  N = int(input())

  flag = False
  if N%3 == 0:
    flag = True
    dig = 0
  else:
    tmpS = str(N)
    n = len(tmpS)
    S = []
    for i in range(n):
      S.append(str(int(tmpS[i])%3))
    if S.count('0')!=0 or (S.count('1')!=0 and S.count('2')!=0):
      flag = True
      dig = max(S.count('1'), S.count('2')) - min(S.count('1'), S.count('2'))
  if flag:
    print(dig)
  else:
    print(-1)

if __name__ == "__main__":
    main()
