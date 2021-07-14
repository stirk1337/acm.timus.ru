n = int(input())
s = input()
s1 = input()
s2 = input()
ch = 1
symb = 3
right1 = 0
right2 = 0
left1 = 0
left2 =0
nechetnie_left = 0
nechetnie_right = 0
chetnie_right = 0
chetnie_left = 0
for i in range(int(n/2)):
	if s[symb] == ">":
		right1 += 1
	else:
		left1 += 1
	symb += 5  

for i in range(int(n/2)):
	if s[symb] == ">":
		right2 += 1
	else:
		left2 += 1
	symb += 5



if left1+right2 < left2+right1:
	var1 = left1+right2
else:
	var1 = left2+right1

symb = 3
for i in range(n):
	if s[symb] == ">" and ch % 2 != 0:
		nechetnie_right += 1
	elif s[symb] == ">" and ch % 2 == 0:
		chetnie_right += 1
	elif s[symb] == "." and ch % 2 != 0:
		nechetnie_left +=1
	elif s[symb] == "." and ch % 2 == 0:
		chetnie_left += 1
	symb += 5
	ch +=1


if chetnie_left+nechetnie_right < chetnie_right+nechetnie_left:
	var2 = chetnie_left+nechetnie_right
else:
	var2 = chetnie_right+nechetnie_left

if var1 > var2:
	print(var2)
else:
	print(var1)





