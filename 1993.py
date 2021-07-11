s = input().split(',')

if len(s) == 2:
	left = s[0].find("{")
	right = s[0].find("}")
	print(s[0][left+1:right].capitalize(), end = " ")
	left = s[0].find("(")
	right = s[0].find(")")
	print(s[0][left+1:right].lower(), end = " ")
	left = s[0].find("[")
	right = s[0].find("]")
	print(s[0][left+1:right].lower()+",", end = "")
	so = 0
	while s[1][so] != "[" and s[1][so] != "(" and s[1][so] != "{":
		so+= 1
	print(s[1][:so], end = "")


	left = s[1].find("{")
	right = s[1].find("}")
	print(s[1][left+1:right].lower(), end = " ")
	left = s[1].find("(")
	right = s[1].find(")")
	print(s[1][left+1:right].lower(), end = " ")
	left = s[1].find("[")
	right = s[1].find("]")
	print(s[1][left+1:right].lower(), end = "")
else:
	left = s[0].find("{")
	right = s[0].find("}")
	print(s[0][left+1:right].capitalize(), end = " ")
	left = s[0].find("(")
	right = s[0].find(")")
	print(s[0][left+1:right].lower(), end = " ")
	left = s[0].find("[")
	right = s[0].find("]")
	print(s[0][left+1:right].lower(), end = "")
