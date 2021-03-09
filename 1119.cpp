#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define ALL(v) v.begin(), v.end() 
#define sort(v) sort(ALL(v)) 
#define reverse(v) reverse(ALL(v)) 
#define foor(i,n) for(int i = 0; i < n; i++)

typedef long long ll;
typedef vector<int> vi;

//start
int diag[1005][1005];
double dp[1005][1005];
int main()
{
	int m, n;
	cin >> n >> m; m++; n++;
	int k;
	int x, y;
	cin >> k;
	foor(i, k)
	{
		cin >> x >> y; x--; y--;
		diag[y][x] = 1;
	}
	/*foor(i, m) {
		foor(j, n)
			cout << diag[i][j] << " ";
		cout << endl;
	}*/

	dp[0][0] = 0;
	for (int i = 1; i < n; i++)
		dp[0][i] = dp[0][i-1] + 100;
	for (int i = 1; i < m; i++)
		dp[i][0] = dp[i-1][0] + 100;
	/*foor(i, m)
	{
		foor(j, n)
			cout << dp[i][j] << " ";
		cout << endl;
	}*/

	for(int i = 1; i < m; i++)
		for (int j = 1; j < n; j++)
		{
			dp[i][j] = min(dp[i - 1][j]+100, dp[i][j - 1]+100);
			if (diag[i-1][j-1] == 1)
				dp[i][j] = min(dp[i][j], dp[i-1][j-1]+100*sqrt(2));	
		}	
	/*foor(i, m)
	{
		foor(j, n)
			cout << dp[i][j] << " ";
		cout << endl;
	}
	*/
	cout << round(dp[m-1][n-1]);

}