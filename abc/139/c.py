def main():
    # input
    N = int(input())
    Hs = [*map(int, input().split())]
  
    # compute
    cnts = [1] * N
    for i in range(N-1):
        if Hs[i] >= Hs[i+1]:
            cnts[i+1] += cnts[i]
  
    # output
    print(max(cnts) - 1)
  
  
if __name__ == '__main__':
    main()
