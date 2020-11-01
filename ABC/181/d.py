def main():
  S = str(input())
  print(type(S), S)

  N = len(S)
  octjudge = [['1', '0', '4'], ['1', '1', '2'], ['1', '2', '0'], ['1', '2', '8'], ['1', '3', '6'], ['1', '4', '4'], ['1', '5', '2'], ['1', '6', '0'], ['1', '6', '8'], ['1', '7', '6'], ['1', '8', '4'], ['1', '9', '2'], ['2', '0', '0'], ['2', '0', '8'], ['2', '1', '6'], ['2', '2', '4'], ['2', '3', '2'], ['2', '4', '0'], ['2', '4', '8'], ['2', '5', '6'], ['2', '6', '4'], ['2', '7', '2'], ['2', '8', '0'], ['2', '8', '8'], ['2', '9', '6'], ['3', '0', '4'], ['3', '1', '2'], ['3', '2', '0'], ['3', '2', '8'], ['3', '3', '6'], ['3', '4', '4'], ['3', '5', '2'], ['3', '6', '0'], ['3', '6', '8'], ['3', '7', '6'], ['3', '8', '4'], ['3', '9', '2'], ['4', '0', '0'], ['4', '0', '8'], ['4', '1', '6'], ['4', '2', '4'], ['4', '3', '2'], ['4', '4', '0'], ['4', '4', '8'], ['4', '5', '6'], ['4', '6', '4'], ['4', '7', '2'], ['4', '8', '0'], ['4', '8', '8'], ['4', '9', '6'], ['5', '0', '4'], ['5', '1', '2'], ['5', '2', '0'], ['5', '2', '8'], ['5', '3', '6'], ['5', '4', '4'], ['5', '5', '2'], ['5', '6', '0'], ['5', '6', '8'], ['5', '7', '6'], ['5', '8', '4'], ['5', '9', '2'], ['6', '0', '0'], ['6', '0', '8']]
  if N == 1:
    if S == '8':
      print('Yes')
      exit()
  elif N == 2:
    if S=='16' or S=='24' or S=='32' or S=='40' or S=='48' or S=='56' or S=='64' or S=='72' or S=='80' or S=='88' or S=='96':
      print('Yes')
      exit()
  else:
    for i in range(64):
      if S in octjudge[i]:
        print('Yes')
        exit()
  print('No')

if __name__ == "__main__":
    main()
