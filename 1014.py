n = int(input())
ls = []
valid = True
if n == 0:
	print(10)
elif n == 1:
	print(1)
else:
	while valid == True and n!= 1:
		valid = False
		for i in range(9,1,-1):
			if n % i == 0:
				valid = True
				ls.append(str(i))
				n /= i
				break
	if valid != True:
		print(-1)
	else:
		for i in range(len(ls)-1, -1, -1):
			print(ls[i], end='')
