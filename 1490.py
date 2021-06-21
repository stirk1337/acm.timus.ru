from math import sqrt, floor, ceil
R = int(input())
ans = R
for i in range(1,R):
	s = ceil(sqrt((R * R) - (i * i)))
	ans += s

print(ans*4)
