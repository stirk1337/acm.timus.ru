devices = []
prices = []
count = []
for i in range(6):
	name = input()
	device = input()
	price = int(input())
	if device not in devices:
		devices.append(device)
		count.append(1)
		prices.append(price)
	else:
		count[devices.index(device)] += 1
		if price < prices[devices.index(device)]:
			prices[devices.index(device)] = price

for i in range(len(count)):
		for j in range(1+i,len(count)):
			if int(count[i]) > int(count[j]):
				count[i], count[j] = count[j], count[i]
				prices[i], prices[j] = prices[j], prices[i]
				devices[i], devices[j] = devices[j], devices[i]
devices.reverse()
count.reverse()
prices.reverse()

mims = []
most = count.count(count[0])
minprice = prices[0]
indexofminprice = 0
if most-1 == 0:
	print(devices[0])
else:
	for i in range(most):
		if prices[i] < minprice:
			indexofminprice = i
			minprice = prices[i]
	print(devices[indexofminprice])

