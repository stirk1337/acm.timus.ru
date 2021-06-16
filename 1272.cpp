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
bool used[10005];
vi g[10005];
int ans = 0;
void dfs(int v){
	used[v] = 1;
	for (int i = 0; i < g[v].size(); i++)
	{
		int to = g[v][i];
		if (!used[to])
		{
			used[to] = 1;
			dfs(to);
		}
	}
	
}

int main()
{
	int n, k,  m;
	scanf("%d%d%d" ,&n, &k, &m);
	for(int i = 0; i < k; i++)
	{ 
		int a, b;
		scanf("%d%d", &a, &b);
		g[a-1].pb(b-1);
		g[b-1].pb(a-1);
	}

	for (int i = 0; i < n; i++) {
		if (!used[i]) {
			dfs(i);
			ans++;
		}
	}
	printf("%d", ans-1);

}
