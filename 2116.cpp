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
int dx[8];
int dy[8];
bool used[105][105];
void dfs(int x, int y, int n) {
	used[x][y] = 1;
	for (int d = 0; d < 8; ++d) {
		int nx = x + dx[d];
		int ny = y + dy[d];
		if (nx >= 0 && nx < n && ny >= 0 && ny < n && !used[nx][ny]) {
			dfs(nx, ny, n);
		}
	}
}
int main()
{
	ll n;
	int a, b;
	int ans = 0;
	cin >> n;
	cin >> a >> b;
	dx[0] = a; dx[1] = a; dx[2] = -a; dx[3] = -a;
	dx[4] = b; dx[5] = b; dx[6] = -b; dx[7] = -b;
	dy[0] = b; dy[1] = -b; dy[2] = b; dy[3] = -b;
	dy[4] = a; dy[5] = -a; dy[6] = a; dy[7] = -a;
	if (a == 0 && b == 0)
	{
		cout << n * n;
		return 0;
	}
	if (n > 100)
		n = 100;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (!used[i][j])
			{
				dfs(i, j, n);
				ans++;
			}
		}
	}
	cout << ans;

}
