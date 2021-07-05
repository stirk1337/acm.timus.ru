from math import sqrt
l, h, w = map(int, input().split())
l = l/100
h = h/100
w = w/60
if l/2 >= h:
	print("butter")
else:
	h = h - l/2
	t = sqrt((2*h)/9.81)
	n = w*t
	while n > 1:
		n = n - 1
	if ((n>=0) and (n <= 0.25)) or ((n >= 0.75) and (n<=1)): 
		print("butter")
	else: 
		print("bread")
