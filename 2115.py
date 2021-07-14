import sys
n = int(input())
m = list(map(int, input().split()))
g = m.copy()
g.sort()
if g == m:
	print("Nothing to do here")
	sys.exit()
g.reverse()
if g == m:
	print("Nothing to do here")
	sys.exit()
swapped = list()

for i in range(n):
	if m[i] == g[i]:
		continue
	else:

		swapped.append(i+1)

if len(swapped) == 2:
	print("Yes")
	print(
		*swapped)
	sys.exit()
else:
	g.reverse()
	if g == m:
		print("Nothing to do here")
		sys.exit()
	swapped.clear()
	for i in range(n):
		if m[i] == g[i]:
			continue
		else:
			swapped.append(i+1)

	if len(swapped) == 2:
		print("Yes")
		print(*swapped)
		sys.exit()
	if len(swapped) > 2:
		print("No hope")
	else:
		print("Nothing to do here")
