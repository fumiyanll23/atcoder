def main():
  # input
  N = int(input())

  # compute
  flag = True
  S = str(N)
  n = len(S)
  digsum, one, two = 0, 0, 0
  ## compute sum of every digit
  for i in range(n):
    digsum += int(S[i])
    ### count the number of '1' and '2'
    if int(S[i])%3 == 1:
      one += 1
    elif int(S[i])%3 == 2:
      two += 1
  ## surplus class of 3
  if digsum%3 == 0:
    dig = 0
  elif digsum%3 == 1:
    if one != 0:
      if n > 1:
        dig = 1
      else:
        flag = False
    else:
      if n > 2:
        dig = 2
      else:
        flag = False
  else:
    if two != 0:
      if n > 1:
        dig = 1
      else:
        flag = False
    else:
      if n > 2:
        dig = 2
      else:
        flag = False

  # output
  if flag:
    print(dig)
  else:
    print(-1)

if __name__ == "__main__":
    main()
