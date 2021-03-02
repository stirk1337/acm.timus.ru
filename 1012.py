n = int(input())
k = int(input())
k-=1
dp = list()
dp.append(0)
dp.append(k)
for i in range(2, n+1):
	dp.append(k*dp[i-1] + k * dp[i-2])
print(dp[n] + dp[n-1])
