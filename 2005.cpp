#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define ALL(v) v.begin(), v.end() 
#define SORT(v) sort(ALL(v)) 
#define REVERSE(v) reverse(ALL(v)) 
#define foor(i,n) for(int i = 0; i < n; i++)

typedef long long ll;
typedef vector<int> vi;

//start
int main()
{
	int m[5][5];
	foor(i, 5)
		foor(j, 5)
			cin >> m[i][j];
	int minimum = m[0][1] + m[1][2] + m[2][3] + m[3][4];
	string answer = "1 2 3 4 5";
	int rast = m[0][3] + m[3][2] + m[2][1] + m[1][4];
	if (rast < minimum)
	{
		minimum = rast;
		answer = "1 4 3 2 5";
	}
	rast = m[0][2] + m[2][1] + m[1][3] + m[3][4];
	if (rast < minimum)
	{
		minimum = rast;
		answer = "1 3 2 4 5";
	}
	rast = m[0][2] + m[2][3] + m[3][1] + m[1][4];
	if (rast < minimum)
	{
		minimum = rast;
		answer = "1 3 4 2 5";
	}
	cout << minimum << endl << answer;
}
