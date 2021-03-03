base = []
requests = []

n = int(input())
for i in range(n):
	base.append(int(input()))

base.sort()
input()

n = int(input())
for i in range(n):
	print(base[int(input())-1])