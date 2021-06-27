from math import floor
n, k = map(int, input().split())
nums = list(map(int, input().split()))
tmp = 0
g = int(n/k)
if n % k == 0:
	pass
else:
	g+=1
for i in range(g):
	for j in range(k):
		tmp = j * g
		try:
			if nums[i +tmp] > 99:
				print(" " + str(nums[i+tmp]), end = "")
				continue
			if nums[i +tmp] > 9:
				print("  " + str(nums[i+tmp]), end = "")
				continue
			else:
				print("   " + str(nums[i+tmp]), end = "")
				continue
		except:
			break
	print()
	
