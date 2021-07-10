n, k = map(int, input().split())
exc = 0
pref = 0
for i in range(n):
	a, b = map(int, input().split())
	exc += a-2
	pref += b

exc+=k-2

ans = exc - pref
if ans < 0:
	print("Big Bang!")
else:
	print(ans)
