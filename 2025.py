t = int(input())
for i in range(t):
	n, k = map(int, input().split())
	full = n // k
	fost = n % k
	print((full*(n-full)*(k-fost)+(full+1)*(n-full-1)*fost)//2)
