
n = int(input())
sol = 0
s = input().split()

for i in range(len(s)):
	for j in range(1+i,len(s)):
		if int(s[i]) > int(s[j]):
			s[i], s[j] = s[j], s[i]


s[len(s) - 1] = int(s[len(s) - 1]) * 2

for i in s:
	sol += int(i)

print(sol)
