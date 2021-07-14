name = []
date = []
result = []
n = int(input())
for i in range(n):
	nametmp = input()
	x = nametmp + " " *(30-len(nametmp))
	name.append(x)
	date.append(input())
	p, s = map(int, input().split())
	restmp = []
	for i in range(p):
		restmp.append(0)
	for i in range(s):
		res = input()
		z = res[:1]
		v = res[2:len(res)]
		if restmp[ord(z)-ord('A')] != "Accepted":
			restmp[ord(z)-ord('A')] = v
	resik = ""
	for i in range(p):
		if restmp[i] == "Accepted":
			resik+="o"
		elif restmp[i] == "Wrong Answer" or restmp[i] == "Time Limit Exceeded" or restmp[i] == "Memory Limit Exceeded" or restmp[i] == "Runtime Error" or restmp[i] == "Compilation Error":
			resik+="x"
		else:
			resik+="."
	result.append(resik)


print("+------------------------------+--------+-------------+")
print("|Contest name"+(" "*18)+"|Date"+"    "+"|"+"ABCDEFGHIJKLM"+"|")
for i in range(n):
	print("+------------------------------+--------+-------------+")
	print("|"+name[i]+"|"+date[i]+"|"+result[i]+ (" "*(13-len(result[i])))+"|")
print("+------------------------------+--------+-------------+")
