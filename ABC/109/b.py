N = int(input())
W = []
for i in range(N):
  W.append(str(input()))

flag = True
for i in range(1, N):
	if W[i-1][-1] != W[i][0]:
		print('No')
		exit()
	for j in range(i-1):
		if W[j] == W[i]:
			print('No')
			exit()

print('Yes')