# definitioin function palindromeChecker()
def palindromeChecker(S, N): # N is required to be odd.
  flag = True
  half = N // 2
  for i in range(half):
    if S[i] != S[-(i+1)]:
      flag = False
  return flag

def main():
  # input
  S = str(input())

  # compute
  N = len(S)
  T = S[:(N-1)//2]
  M = len(T)
  U = S[(N+3)//2 - 1:]
  O = len(U)
  a = palindromeChecker(S, N)
  b = palindromeChecker(T, M)
  c = palindromeChecker(U, O)

  # output
  if a and b and c:
    print('Yes')
  else:
    print('No')


if __name__ == "__main__":
    main()
