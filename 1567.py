stroka = str(input())
summa = 0
odin_r = ["a", "d", "g", "j", "m", "p", "s", "v", "y", ".", " "]
dva_r = ["b", "e", "h", "k", "n", "q", "t", "w", "z", ","]
tri_r = ["c", "f", "i", "l", "o", "r", "u", "x", "!"]
for i in range(int(len(stroka))):
	if stroka[i] in odin_r:
		summa += 1
	elif stroka[i] in dva_r:
		summa += 2
	elif stroka[i] in tri_r:
		summa += 3

print(summa)
