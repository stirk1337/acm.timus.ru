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
int v1, v2;
vi g[1005];
bool used[1005];
bool edges[1005][1005];
int rebra;
void dfs(int v) {
	used[v] = true;
	for (int i = 0; i < g[v].size(); i++)
	{
		int to = g[v][i];
		if (!edges[v][to])
		{
			rebra++;
			edges[v][to] = 1;
			edges[to][v] = 1;
		}
		if (!used[to])
		{
			dfs(to);
		}
	}

}

int main()
{
	while (cin >> v1)
	{
		cin >> v2;
		g[v1-1].pb(v2-1);
		g[v2-1].pb(v1-1);
	}
	int ans = 0;
	foor(i, 1000)
	{
		if (!used[i])
		{
			dfs(i);
			if (rebra != 0)
			{
				if (rebra % 2 != 0)
				{
					cout << 0;
					return 0;
				}
				rebra = 0;
			}
			
			
		}
	}
	cout << 1;
}
