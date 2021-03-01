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
int main()
{
	int n, k;
	int dp[20];
	scanf("%d%d", &n, &k); k--;
	dp[0] = 0; dp[1] = k;
	for (int i = 2; i <= n; i++)
	{
		dp[i] = k * dp[i - 1] + k * dp[i - 2];
	}
	printf("%d", dp[n] + dp[n - 1]);
}