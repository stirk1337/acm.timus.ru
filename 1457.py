n = int(input())
s = input().split()
summa = 0
for i in range(len(s)):
	summa += int(s[i])

print(round(summa/n,6))
