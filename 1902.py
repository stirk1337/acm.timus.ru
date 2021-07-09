n, t, s = map(int, input().split())
cars = list(map(int, input().split()))
for i in range(n):
	print((float(cars[i]+t+s)/2))
