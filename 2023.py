n = int(input())
l1 = ["Alice", "Ariel", "Aurora", "Phil", "Peter", "Olaf", "Phoebus", "Ralph", "Robin"]
l2 = ["Bambi", "Belle", "Bolt", "Mulan", "Mowgli", "Mickey", "Silver", "Simba", "Stitch"]
l3 = ["Dumbo", "Genie", "Jiminy", "Kuzko", "Kida", "Kenai", "Tarzan", "Tiana", "Winnie"]
solution = 0
place = 1
for i in range(n):
	letter = input()
	if letter in l1 and place == 1:
		pass
	elif letter in l2 and place == 1:
		solution += 1
		place = 2
	elif letter in l3 and place == 1:
		solution += 2
		place = 3
	elif letter in l1 and place == 2:
		solution += 1
		place = 1
	elif letter in l2 and place == 2:
		pass
	elif letter in l3 and place == 2:
		solution += 1
		place = 3
	elif letter in l1 and place == 3:
		solution += 2
		place = 1
	elif letter in l2 and place == 3:
		solution += 1
		place = 2
	elif letter in l3 and place == 3:
		pass

print(solution)
		
