#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define pb push_back
#define all(v) v.begin(), v.end() 
#define reverse(v) reverse(all(v)) 

#define x first.first 
#define y first.second 
#define d second.first 
#define s second.second 

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;


const ll INF = 1e12;
//start
ll dp[10005][2];
pair<pair<ll, ll>, pair<ll, string>> a[10005];
int main() {
	//freopen("input.txt", "r", stdin);
	ll n, m;
	cin >> n >> m;
	for (int i = 1; i <= n; i++)
		dp[i][0] = dp[i][1] = INF;

	dp[1][1] = 0;
	dp[1][0] = 0;
	for (int i = 1; i <= m; i++)
		cin >> a[i].x >> a[i].y >> a[i].d >> a[i].s;
	sort(a + 1, a + m + 1);

	for (int i = 1; i <= m; i++) {
		if (a[i].s == "Licensed") {
			dp[a[i].y][0] = min(dp[a[i].x][0] + a[i].d, dp[a[i].y][0]);
		}
		if (a[i].s == "Pirated") {
			dp[a[i].y][1] = min(dp[a[i].x][1] + a[i].d, dp[a[i].y][1]);
			dp[a[i].y][1] = min(dp[a[i].x][0] + a[i].d, dp[a[i].y][1]);
		}
		if (a[i].s == "Cracked") {
			dp[a[i].y][0] = min(dp[a[i].x][0] + a[i].d, dp[a[i].y][0]);
			dp[a[i].y][1] = min(dp[a[i].x][1] + a[i].d, dp[a[i].y][1]);
		}
		//cout << dp[a[i].y][0] << endl << dp[a[i].y][1] << endl;
	}

	ll ans = min(dp[n][0], dp[n][1]);
	if (ans == INF)
		cout << "Offline";
	else
		cout << "Online" << "\n" << ans;
}
