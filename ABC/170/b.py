X, Y = map(int, input().split())

for i in range(50):
  for j in range(50):
    if(i+j == X and 2*i+4*j == Y):
      print("Yes")
print("No")

# In case, print "Yes" and "No".