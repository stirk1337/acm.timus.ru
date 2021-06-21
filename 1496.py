sumbits = []
spamers = []
n = int(input())
solution = 0

for i in range(n):
	sumbit = input()
	if sumbit in sumbits:
		if sumbit in spamers:
			pass
		else:
			spamers.append(sumbit)
	else:
		sumbits.append(sumbit)

for i in range(int(len(spamers))):
	print(spamers[i])
