n, k = map(int, input().split())
s = input().split()
sum = 0
for i in range(len(s)):
	sum += int(s[i])
	if (sum - n) >= 0:
		sum -= n
	else:
		sum = 0
print(sum)
