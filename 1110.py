numbers = input()
numbers = numbers.split()
solutions = [""]
once = 1
N = int(numbers[0])
M = int(numbers[1])
Y = int(numbers[2])

for X in range(M-1):
	if (X ** N) % M == Y:
		if once == 1:
			solutions[0] = X
			once = 0
		else:
			solutions.append(X)


if N == 1 and M == 2 and Y == 1:
	print(1)
elif solutions[0] == "":
	print(-1)
else:
	print(*solutions)