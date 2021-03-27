### TLE ......

def lucas_number(N: int) -> int:
  if N == 0:
    return 2
  elif N == 1:
    return 1
  elif N >= 2:
    return lucas_number(N-1) + lucas_number(N-2)


def main():
  # input
  N = int(input())

  # output
  print(lucas_number(N))

if __name__ == "__main__":
    main()
