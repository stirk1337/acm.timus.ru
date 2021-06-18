n = int(input())
a = list()
for i in range(n):
	a.append([0]*n)
j = 1

for i in range(((n-1)*2)+1):
	for x in range(i, -1, -1):
		if x<n and i-x<n:
			a[i-x][x]= j
			j+=1
			

for i in range(n):
	for x in range(n-1,-1,-1):
		print(a[i][x], end = " ")
	print()
