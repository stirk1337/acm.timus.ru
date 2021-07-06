gold, silver, bronze, win = [], [], [], []
for i in range(4):
	gold.append(input())
for i in range(4):
	silver.append(input())
for i in range(4):
	bronze.append(input())

for i in range(int(input())):
	w = 0
	for j in range(int(input())):
		vuz, rank = input().split(":")
		vuz = vuz[:len(vuz)-1]
		rank = rank[1:len(rank)]
		if rank == "gold":
			if vuz in gold:
				w+=1
		elif rank == "silver":
			if vuz in silver:
				w+=1
		elif rank == "bronze":
			if vuz in bronze:
				w+=1
	win.append(w)

print(win.count(max(win))*5)
