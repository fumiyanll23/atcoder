P, Q, R = map(int, input().split())

time = [P+Q, Q+R, R+P]
print(min(time))