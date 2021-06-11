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
int w[101];
int dp[100001][101];
bool marked[101];
bool noans = 0;
void getAns(int i, int j) {
	//cout << dp[i][j] << endl;
	if (dp[i][j] == 0)
		return;
	if (dp[i][j] == dp[i][j - 1] && dp[i][j] == dp[i - w[j]][j - 1] + w[j])
		noans = 1;
	if (dp[i][j - 1] == dp[i][j])
		getAns(i, j - 1);
	else
	{
		getAns(i - w[j], j - 1);
		//cout << j << " ";
		marked[j] = 1;
	}
}

int main()
{
	int n, s;
	scanf("%d%d", &s, &n); n++; s++;

	for (int i = 1; i < n; i++)
		scanf("%d", &w[i]);


	for (int i = 1; i < s; i++) {
		for (int j = 1; j < n; j++) {
			if (i - w[j] >= 0)
				dp[i][j] = max(dp[i][j - 1], dp[i - w[j]][j - 1] + w[j]);
			else
				dp[i][j] = dp[i][j - 1];
		}
	}

	getAns(s-1, n-1);
	if (dp[s - 1][n - 1] != s - 1) {
		printf("%d", 0);
		return 0;
	}
	if (noans) {
		printf("%d", -1);
		return 0;
	}
	for (int i = 1; i < n; i++) {
		//cout << marked[i] << endl;
		if (!marked[i])
			printf("%d ", i);
	}

	/*for (int i = 0; i < s; i++) {
		for (int j = 0; j < n; j++)
			cout << dp[i][j] << " ";
		cout << endl;
	}*/

}
