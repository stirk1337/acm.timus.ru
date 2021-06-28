import sys
g = 1
for line in sys.stdin:
	for i in range(len(line)):
		if ord(line[i]) == 10:
			print()
		elif g == 1:
			print(line[i].upper(), end = "")
			if line[i].isalpha():
				g = 0
		elif line[i].isalpha():
			print(line[i].lower(), end = "")
		else:
		 	print(line[i], end = "")
		 	if line[i] == "." or line[i] == "?" or line[i] == "!":
		 		g = 1
