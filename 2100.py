n = int(input())
money = 200
for i in range(n):
	name = str(input())
	if "+" in name:
		money += 200
	else:
		money += 100

if money == 1300:
	money = 1400
print(money)
