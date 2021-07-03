import sys
def filtminus(x):
	if x < 0:
		return 1
	else:
		return 0

def filtplus(x):
	if x > 0:
		return 1
	else:
		return 0

n, x = map(int, input().split())
stop = list(map(int, input().split()))
right = list(filter(filtplus, stop))
if len(right) == 0:
	right.append(1001)
right = min(right)
left = list(filter(filtminus, stop))
if len(left) == 0:
	left.append(-1001)
left = max(left)
if x >= right or x <= left:
	print("Impossible")
else:
	if x < 0:
		print(right+right+abs(x), abs(x))
	else:
		print(x, abs(left)+abs(left)+x)
