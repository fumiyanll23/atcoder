def main():
  # input
  X, Y = map(str, input().split())

  # output
  if ord(X) < ord(Y):
    print('<')
  elif ord(X) > ord(Y):
    print('>')
  else:
    print('=')

if __name__ == "__main__":
    main()
