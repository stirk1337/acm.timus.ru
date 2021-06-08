g = set()
g.add(input())
while True:
	inp = input().split('-')
	if len(inp) == 1:
		break
	g.add(inp[0])
	g.add(inp[1])
print(len(g)-1)
