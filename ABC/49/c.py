def main():
  S = str(input())

  N = len(S)
  T = ''
  n = len(T)
  start = 0
  while N > n:
    if S[start:start+5]=='dream':
      start += 5
      T += 'dream'
    elif S[start:start+7]=='dreamer':
      start += 7
      T += 'dreamer'
    elif S[start:start+5]=='erase':
      start += 5
      T += 'erase'
    elif S[start:start+6]=='eraser':
      start += 6
      T += 'eraser'
    if S == T:
      print('Yes')
      exit()
  print('No')

if __name__ == "__main__":
    main()

### I don't know...
