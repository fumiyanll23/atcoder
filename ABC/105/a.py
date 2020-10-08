N, K = map(int, input().split())

div = N // K
mod = N % K
print(min(mod, abs(div+1-mod)))

### This code is WRONG:(