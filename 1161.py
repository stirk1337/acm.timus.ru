from math import sqrt
n = int(input())
a = []
for i in range(n):
	a.append(int(input()))
a.sort()
a.reverse()
minn = 999999999999999
for i in range(n-1):
	if len(a) > 1:
		a[0] = 2*sqrt(a[0]*a[1])
		del a[1]
	else:
		break
print(a[0])
