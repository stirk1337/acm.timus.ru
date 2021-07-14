def translate(number_old):
	steps = []
	number = number_old
	newnum = number//(256**3)
	if newnum < 1:
		steps.append(0)
		pass
	else:
		steps.append(number//(256**3))
		number = number - (256**3)*(number//(256**3)) #!
	newnum = number//(256**2)
	if newnum < 1:
		steps.append(0)
		pass
	else:
		steps.append(number//(256**2))
		number = number - (256**2)*(number//(256**2)) #!
	newnum = number//(256)
	if newnum < 1:
		steps.append(0)
		pass
	else:
		steps.append(number//(256))
		number = number - (256)*(number//256)
	steps.append(number)
	return steps

pc = input()
number_old = int(input())
steps = translate(number_old)
if pc == "GOOD":
	steps.reverse()
	print(steps[0]*(256**3)+steps[1]*(256**2)+steps[2]*(256)+steps[3]*1)
else:
	print(steps[0]*1+steps[1]*(256)+steps[2]*(256**2)+steps[3]*(256**3))
