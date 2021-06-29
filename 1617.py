n = int(input())
kolesa = []
solution = 0
for i in range(n):
	koleso = input()
	kolesa.append(koleso)
lenght = len(kolesa)
i = 0
while i != lenght:
	#print(i, lenght)
	#print(kolesa[i])
	#print(kolesa)
	if kolesa.count(kolesa[i]) >= 4:
		#print('i am there')
		solution += 1
		tmp = kolesa[i]
		for j in range(4):
			kolesa.remove(tmp)
		lenght = len(kolesa)
		i = -1
		#print(i)
	i += 1


print(solution)
