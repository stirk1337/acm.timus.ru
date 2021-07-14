#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define ALL(v) v.begin(), v.end() 
#define sort(v) sort(ALL(v)) 
#define reverse(v) reverse(ALL(v)) 
#define foor(i,n) for(int i = 0; i < n; i++)

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef string str;

//start
map <string, int> number;
vi g[1005];
vs names;
int hp[1005];
bool used[1005];
vi team;
vi teams[1005];
void dfs(int v) {
	used[v] = true;
	team.push_back(v);
	for (int i = 0; i < g[v].size(); i++)
	{
		int to = g[v][i];
		if (!used[to])
			dfs(to);
	}
}

int main()
{
	int n;
	cin >> n;
	foor(i, n)
	{
		hp[i] = 3;
		string name;
		cin >> name;
		number[name] = i;
		names.pb(name);
	}
	int k;
	cin >> k;
	foor(i, k)
	{
		string name, name2, log, in, emp;
		cin >> name >> log;
		int first = number[name];
		if (log == "HIT")
		{
			cin >> name2 >> emp >> in;
			int second = number[name2];
			if (hp[first] < 2)
			{
				cout << "FAKE";
				return 0;
			}
			if (in == "HEAD")
			{
				hp[second] = max(0, hp[second] - 2);
			}
			else
			{
				hp[second] = max(0, hp[second] - 1);
			}

		}
		if (log == "USES")
		{
			cin >> emp;
			if (hp[first] < 2)
			{
				cout << "FAKE";
				return 0;
			}
			hp[first] = 3;
		}
		if (log == "REVIVE")
		{
			if (hp[first] < 2)
			{
				cout << "FAKE";
				return 0;
			}
			string name2;
			cin >> name2;
			int second = number[name2];
			if (hp[second] != 1)
			{
				cout << "FAKE";
				return 0;
			}
			hp[second] = 2;
			g[first].pb(second);
			g[second].pb(first);
		}

	}
	int comp = 0;
	int a = 0;
	foor(i, n)
	{
		if (!used[i])
		{
			team.clear();
			dfs(i);
			//cout << "Team: ";
			foor(j, team.size())
			{
				teams[a].pb(team[j]);
				//cout << " " << teams[a][j];
			}
			a++;
			comp++;
			//cout << endl;
			if (teams[a-1].size() > 4)
			{
				cout << "FAKE";
				return 0;
			}
		}
	}
	//cout << comp;
	vi teamsize4, teamsize3, teamsize2, teamsize1;
	for (int i = 0; i < comp; i++)
	{
		if (teams[i].size() == 4)
			teamsize4.pb(i);
		if (teams[i].size() == 3)
			teamsize3.pb(i);
		if (teams[i].size() == 2)
			teamsize2.pb(i);
		if (teams[i].size() == 1)
			teamsize1.pb(i);
	}
	if (teamsize1.size() < teamsize3.size())
	{
		cout << "FAKE";
		return 0;
	}
	cout << "CORRECT" << endl;
	for (int i = 0; i < teamsize4.size(); i++)
	{
		for (int j = 0; j < teams[teamsize4[i]].size(); j++)
			cout << names[teams[teamsize4[i]][j]] << " ";
		cout << endl;
	}

	for (int i = 0; i < teamsize3.size(); i++)
	{
		for (int j = 0; j < teams[teamsize3[i]].size(); j++)
			cout << names[teams[teamsize3[i]][j]] << " ";
		cout << names[teams[teamsize1[0]][0]] << endl;
		teamsize1.erase(teamsize1.begin());
	}
	while (teamsize2.size() >= 2)
	{
		cout << names[teams[teamsize2[0]][0]] << " " << names[teams[teamsize2[0]][1]] << " " << names[teams[teamsize2[1]][0]] << " " << names[teams[teamsize2[1]][1]] << endl;
		teamsize2.erase(teamsize2.begin());
		teamsize2.erase(teamsize2.begin());
	}
	if (teamsize2.size() != 0)
	{
		cout << names[teams[teamsize2[0]][0]]<< " " << names[teams[teamsize2[0]][1]] << " " << names[teams[teamsize1[0]][0]] << " " << names[teams[teamsize1[1]][0]] << endl;
		teamsize1.erase(teamsize1.begin());
		teamsize1.erase(teamsize1.begin());
	}
	if (teamsize1.size() != 0)
	{
		int space = 0;
		
		for (int i = 0; i < teamsize1.size(); i++)
		{
			cout << names[teams[teamsize1[i]][0]] << " ";
			space++;
			if (space == 4) {
				cout << endl;
				space = 0;
			}	
		}
	}
	return 0;
}
