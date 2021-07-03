import sys
n = int(input())
if n == 0:
	print(10)
	sys.exit()
hungry, satisfied = list(), list()
hungry.append(2)
satisfied.append(10)
for i in range(n):
	inp = input().split()
	nut, status = int(inp[0]), inp[1]
	if status == "hungry":
		hungry.append(nut)
	else:
		satisfied.append(nut)

if max(hungry) >= min(satisfied): 
	print("Inconsistent")
else:
	print(min(satisfied))
