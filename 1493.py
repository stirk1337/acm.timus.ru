s = input()

s1 = s[:3]
s2 = s[3:len(s)]
olds2 = s2 
sumpl = 0
summi = 0
dns = 0
s2pl = str(int(s2) + 1)
s2mi = str(int(s2) - 1)

if s2mi == "-1":
	s2mi == 0
	dns = 1
for i in range(len(s2pl)):
	sumpl += int(s2pl[i])
if dns == 0:
	for i in range(len(s2mi)):
		summi += int(s2mi[i])

if sumpl == int(s1[0]) + int(s1[1]) + int(s1[2]):
	print("Yes")
elif summi == int(s1[0]) + int(s1[1]) + int(s1[2]):
	print("Yes")
else:
	print("No")
