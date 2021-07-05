#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define ALL(v) v.begin(), v.end() 
#define SORT(v) sort(ALL(v)) 
#define REVERSE(v) reverse(ALL(v)) 
#define for_i for(int i = 0; i < n; i++)
#define for_j for(int j = 0; j < n; j++)

typedef long long ll;
typedef vector<int> vi;
typedef queue<int> qi;
typedef vector<string> vs;
typedef string str;

//start
const int maxn = 300;
qi turn;
bool used[maxn];
int dst[maxn];
vi g[maxn];
map <string, int> number;
vs names;
int n, start = -1, vi1, vi2, vi3;
str v1, v2, v3;

int getnum(str v) {
	if (number.count(v) > 0)
	{
		return number[v];
	}
	number[v] = number.size();
	names.pb(v);
	return number[v];
}

void bfs(int start) {
	turn.push(start);
	used[start] = 1;
	dst[start] = 1;
	while (!turn.empty())
	{
		int ind = turn.front();
		turn.pop();
		for (int neighbor = 0; neighbor < g[ind].size(); neighbor++)
		{
			if (!used[g[ind][neighbor]])
			{
				turn.push(g[ind][neighbor]);
				used[g[ind][neighbor]] = true;
				dst[g[ind][neighbor]] = dst[ind] + 1;
			}
		}
	}
}
int main() {
	cin >> n;
	for_i
	{
		cin >> v1 >> v2 >> v3;
		vi1 = getnum(v1);
		vi2 = getnum(v2);
		vi3 = getnum(v3);
		if (v1 == "Isenbaev")
			start = vi1;
		if (v2 == "Isenbaev")
			start = vi2;
		if (v3 == "Isenbaev")
			start = vi3;
		g[vi1].push_back(vi2);
		g[vi1].push_back(vi3);
		g[vi2].push_back(vi1);
		g[vi2].push_back(vi3);
		g[vi3].push_back(vi1);
		g[vi3].push_back(vi2);
	}
	if (start != -1)
		bfs(start);

	SORT(names);
	for (int i = 0; i < names.size(); i++)
	{
		if (dst[number[names[i]]] - 1 == -1)
			cout << names[i] << " " << "undefined" << endl;
		else
			cout << names[i] << " " << dst[number[names[i]]] - 1 << endl;
	}
}
