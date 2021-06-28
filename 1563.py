n = int(input())
shops = []
bayan = 0
for i in range(n):
	shop = str(input())
	if shop in shops:
		bayan += 1
	else:
		shops.append(shop)

print(bayan)
