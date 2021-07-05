def summ(k10, k50, k100, k500, k1000, k5000,n):
	return (k10*10+k50*50+k100*100+k500*500+k1000*1000+k5000*5000)//n

k10, k50, k100, k500, k1000, k5000 = map(int, input().split())
n = int(input())
maxsum = summ(k10, k50, k100, k500, k1000, k5000,n)
minsum = maxsum
if k10 != 0:
	k10-=1
	minsum = summ(k10, k50, k100, k500, k1000, k5000,n)
elif k50 != 0:
	k50-=1
	minsum = summ(k10, k50, k100, k500, k1000, k5000,n)
elif k100 != 0:
	k100-=1
	minsum = summ(k10, k50, k100, k500, k1000, k5000,n)
elif k500 != 0:
	k500-=1
	minsum = summ(k10, k50, k100, k500, k1000, k5000,n)
elif k1000 != 0:
	k1000-=1
	minsum = summ(k10, k50, k100, k500, k1000, k5000,n)
elif k5000 != 0:
	k5000-=1
	minsum = summ(k10, k50, k100, k500, k1000, k5000,n)
print(maxsum-minsum)
for i in range(minsum+1, maxsum+1):
		print(i, end = " ")		
