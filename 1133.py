import sys

a = [0]*3005
i, tmp1, j, tmp2, n = map(int, input().split())
i+=1000
a[i] = tmp1
j+=1000
a[j] = tmp2
n+=1000

l = min(i,j)
r = max(i,j)

def binsearch(left, right):
	l = -20000000000
	r = 20000000000
	while(l+1<r):
		mid = (l+r)//2
		#print(l, r)
		#print(mid)
		a[left+1] = a[left] + mid
		for i in range(left+2, right):
			a[i] = a[i-1] + a[i-2]
		if (a[right] == a[right-1] + a[right-2]):
			return 

		#for i in range(left, right+1):
		#	print(a[i], end = " ")
		#print()

		if (a[right] > a[right-1] + a[right-2]):
			l = mid
		else:
			r = mid


if(r == l+1):
	if (n >= r):
		for i in range(r+1, n+1):
			a[i] = a[i-1] + a[i-2]
		print(a[n])
		sys.exit()
	if (n <= l):
		for i in range(l-1, n-1, -1):
			a[i] = a[i+2] - a[i+1]
		print(a[n])
		sys.exit()

binsearch(l,r)

if(n >= r):
	for i in range(r+1, n+1):
		a[i] = a[i-1] + a[i-2]
	print(a[n])
	sys.exit()
if (n <= l):
	for i in range(l-1, n-1, -1):
		a[i] = a[i+2] - a[i+1]
	print(a[n])
	sys.exit()

if (n <= r):
	for i in range(l+2, n+1):
		a[i] = a[i-1] + a[i-2]
	print(a[n])
	sys.exit()
