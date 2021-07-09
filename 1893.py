s = input()

ryad = s[len(s)-1]

s = s.replace(ryad, "")
if int(s) <= 2:
	if ryad == "B" or ryad == "C":
		print("aisle")
	else:
		print("window")

elif int(s) <= 20:
	if ryad == "B" or ryad == "C" or ryad == "D" or ryad == "E":
		print("aisle")
	elif ryad == "A" or ryad == "F":
		print("window")

elif int(s) <= 65:
	if ryad == "C" or ryad == "D" or ryad == "G" or ryad == "H":
		print("aisle")
	elif ryad == "A" or ryad == "K":
		print("window")
	else:
		print("neither")
