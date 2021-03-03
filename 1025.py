k = int(input())

k = int(k/2+1)
sum = 0


groups = input().split()
for i in range(len(groups)):
	groups[i] = int(groups[i])

for i in range(len(groups)):
	for j in range(i+1,len(groups)):
		if groups[i] > groups[j]:
			groups[i], groups[j] = groups[j], groups[i]


for i in range(k):
	sum += int(groups[i]/2+1)

print(sum)