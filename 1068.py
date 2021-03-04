n = int(input())
summa = 0
if n > 0:
	for i in range(n+1):
		summa += i
else:
	for i in range(n,1+1):
		summa += i
print(summa)