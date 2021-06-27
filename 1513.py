n, a = map(int, input().split())
dp = [[0] * 2 for i in range(n+1)]
pref = [[0] * 2 for i in range(n+1)]
dp[0][0] = dp[0][1] = pref[0][0] = pref[0][1] = 1
for i in range(1, n+1):
	if (i-a >= 0):
		dp[i][0] = pref[i-1][1] - pref[i-a-1][1]
		dp[i][1] = pref[i-1][0]
	else:
		dp[i][0] = pref[i-1][1]
		dp[i][1] = pref[i-1][0]

	pref[i][0] = dp[i][0] + pref[i-1][0]
	pref[i][1] = dp[i][1] + pref[i-1][1]

print(dp[n][0] + dp[n][1])
