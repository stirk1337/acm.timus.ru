#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define all(v) v.begin(), v.end() 
#define sort(v) sort(all(v)) 
#define REVERSE(v) reverse(all(v)) 
#define for_i for(int i = 0; i < n; i++)
#define for_j for(int j = 0; j < n; j++)

typedef long long ll;
typedef vector<int> vi;

//start
int main()
{
	int n, v = -1;
	vi g[100];
	vi fteam;
	cin >> n;
	for_i
	{
		while (1)
		{
			cin >> v;
			if (v == 0)
				break;
			g[i].pb(v - 1);
			g[v - 1].pb(i);
		}
	}

	int doo = 1;
	for_i
	{
		if (g[i].size() == 0)
		{
			cout << 0;
			return 0;
		}
		for (int j = 0; j < g[i].size(); j++)
		{
			if (find(fteam.begin(), fteam.end(), g[i][j]) != fteam.end())
			{
				doo = 0;
				break;
			}
		}
		if (doo == 1)
			fteam.pb(i);
		doo = 1;
	}
	
	cout << fteam.size() << endl;
	for (int i = 0; i < fteam.size(); i++)
	{
		cout << fteam[i]+1 << " ";
	}
}