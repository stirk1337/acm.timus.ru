#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define all(v) v.begin(), v.end() 
#define sort(v) sort(ALL(v)) 
#define reverse(v) reverse(ALL(v)) 

typedef long long ll;
typedef vector<int> vi;

//start
ll dp[50005][2];
ll pref[50005][2];
int main()
{
	int n, a, b;
	scanf("%d%d%d", &n, &a, &b);
	dp[0][0] = dp[0][1] = pref[0][0] = pref[0][1] = 1;
	for (int i = 1; i <= n; i++)
	{
		if (i - a >= 0)
			dp[i][0] = pref[i - 1][1] - pref[i - a - 1][1];
		else
			dp[i][0] = pref[i - 1][1];
		if (i - b >= 0)
			dp[i][1] = pref[i - 1][0] - pref[i - b - 1][0];
		else
			dp[i][1] = pref[i - 1][0];

		dp[i][0] %= 1000000007; dp[i][1] %= 1000000007;
		pref[i][0] = dp[i][0] + pref[i - 1][0];
		pref[i][1] = dp[i][1] + pref[i - 1][1];
		//pref[i][0] %= 1000000007; pref[i][1] %= 1000000007;
	}
	printf("%lld", (dp[n][0] + dp[n][1]) % 1000000007);
}
