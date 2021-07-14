v1 = input().split()
x = int(v1[0])
y = int(v1[1])
z = int(v1[2])
v2 = input().split()
a = int(v2[0])
b = int(v2[1])
c = int(v2[2])

k = 1
if x+y+z<a+b+c:
	k = 0
else:
	if x==a and y+z >= b+c or y==b and x+z >=a+c:
		k = 1
	else:
		if x>a and y+z >=b and x-a>=c-(z-b+y) or y>b and x+z>=a and y-b>=c-(z-a+x):
			k = 1
		else:
			if x<a and y<b and z+x-a+y-b>=c:
				k = 1
			else:
				k = 0
if k == 1:
	print("It is a kind of magic")
else:
	print("There are no miracles in life")
