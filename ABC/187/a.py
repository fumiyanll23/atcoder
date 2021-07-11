# input
A, B = map(list, input().split())

# compute
a_sum = sum(map(int, A))
b_sum = sum(map(int, B))

# output
if a_sum >= b_sum:
    print(a_sum)
else:
    print(b_sum)
