n = int(input())
marks = []
sum = 0
sr_arifm = 0
for i in range(n):
	mark = input()
	marks.append(mark)

if "3" in marks:
	print("None")
elif "4" in marks:
	for i in marks:
		sum += int(i)
	sr_arifm = sum/len(marks)
	if sr_arifm >= 4.5:
		print("High")
	else:
		print("Common")
else:
	print("Named")
