def main():
  # input
  N = int(input())

  # compute
  digit = list(map(int, list(str(N))))

  # output
  if digit[0]==digit[1]==digit[2] or digit[1]==digit[2]==digit[3]:
    print('Yes')
  else:
    print('No')

if __name__ == "__main__":
    main()
