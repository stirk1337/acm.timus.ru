#include <bits/stdc++.h>
using namespace std;
vector <int> g[100];
bool used[100];
int col[100];
int gabella = 0;
queue <int> turn;

void bfs(){
	turn.push(0);
	used[0] = true;
	col[0] = 0;
	while(!turn.empty())
	{
		int ind = turn.front();
		turn.pop();
		for(int neighbor = 0; neighbor < g[ind].size(); neighbor++)
		{
			if (!used[g[ind][neighbor]])
			{
				turn.push(g[ind][neighbor]);
				used[g[ind][neighbor]] = true;
				if (col[ind] == 1)
					col[g[ind][neighbor]] = 0;
				else
					col[g[ind][neighbor]] = 1;							
			}
			else
			{
				if (col[ind] == col[g[ind][neighbor]])
					gabella = 1;
					
			}
		}
	}
}

int main(){
	int n, v = -1;
	cin >> n;
	for(int i = 0; i < n; i++)
	{
		col[i] = 2;
	}
	for(int i = 0; i < n; i++)
	{
		while (1)
		{
			cin >> v;
			if (v == 0)
				break;
			g[i].push_back(v-1);
			g[v-1].push_back(i);
		}
	}	
	bfs();
	if (gabella == 0)
	{
		for(int i = 0; i < n; i++)
			cout << col[i];
	}
	else
		cout << -1;
}