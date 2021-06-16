money, lim, cgb = map(int, input().split())
life = 0
while money > lim:
	money = money - (money * (cgb / 100))
	life += 1

print(life)
