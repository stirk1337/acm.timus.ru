"""s, n = map(int, input().split())
summa = 0
x = 0
flag = 0
s *= 3
for i in range(n):
	m = float(input())
	summa += m
	x+=1
	if summa >= s:
		for i in range(n-x):
			input()
		print("Free after", x, "times.")
		flag = 1
		break

if flag == 0:
	print("Team.GOV!")
"""
import sys
n, m = map(int, input().split())
n = n * 3
for i in range(m):
	s = int(input())
	n = n - s
	if n < 0:
		print("Free after", i+1, "times.")
		sys.exit()
print("Team.GOV!")
