n, m = map(int, input().split())
cycle = []
for i in range(n):
	cycle.append(int(input()))

for i in range(m):
	cycle.insert(len(cycle), cycle[0])
	del cycle[0]

for i in range(10): print(cycle[i], end = "")
