vxod = input().split()
a = int(vxod[0])
b = int(vxod[1])
c = int(vxod[2])
d = int(vxod[3])

while c > a:
	a += b
	if a > c:
		a = c
	c -= d
print(a)
