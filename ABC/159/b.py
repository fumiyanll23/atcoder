S = str(input())

N = len(S)
half = (N - 1) / 2 # 半分よりも前
fn = [0 for i in range(half)]
f3 = [0 for i in range(3)]

# The first condition
for i in range(half):
  if S[i] == S[N-1-i]:
    fn[i] += 1
if sum(flag) == n:
  f3[0] = 1

# The second condition
Sp = S[:half-1]

#The third condition
Sn = S[half+1:]

# Get tired...:(