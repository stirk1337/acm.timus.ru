n, k = map(int, input().split())
bumbum = input().split()
bumbumi = 0
solution = 0
for i in range(n):
	if  k - int(bumbum[i]) < 0:
		solution += 0
		bumbumi += int(bumbum[i]) - k
	else:
		solution += k - int(bumbum[i])

print(bumbumi, solution)
