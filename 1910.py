n = int(input())
walls = input().split()
max = 0

for i in range(len(walls)-2):
	sum = int(walls[i]) + int(walls[i+1]) + int(walls[i+2])
	if sum > max:
		max = sum
		mid = i + 2

print(max, mid)
