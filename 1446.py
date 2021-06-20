n = int(input())
Gryffindor = []
Hufflepuff = []
Slytherin = []
Ravenclaw = []
for i in range(n):
	name = input()
	fak = input()
	globals()[fak].append(name)

print('Slytherin:')
for i in Slytherin: print(i)
print()
print('Hufflepuff:')
for i in Hufflepuff: print(i)
print()
print('Gryffindor:')
for i in Gryffindor: print(i)
print()
print('Ravenclaw:')
for i in Ravenclaw: print(i)
