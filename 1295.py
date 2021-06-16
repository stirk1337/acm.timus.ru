n = int(input())
m = 10
x = 0
g = (1 ** n + 2 ** n + 3 ** n + 4 ** n) % m
while g == 0:
	m *= 10
	g = (1 ** n + 2 ** n + 3 ** n + 4 ** n) % m
	x+=1
print(x)
