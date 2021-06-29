qxx, zzz = map(int, input().split())
s = input().split()

sum = 0
for i in range(len(s)):
	sum += int(s[i])

sum = sum * 20

if zzz - sum < qxx:
	print("Dirty debug :(")
else:
	print("No chance.")
