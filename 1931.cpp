#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define ALL(v) v.begin(), v.end() 
#define sort(v) sort(ALL(v)) 
#define reverse(v) reverse(ALL(v)) 
#define foor(i,n) for(int i = 1; i < n; i++)

typedef long long ll;
typedef vector<int> vi;

//start
int ans[100000];
int main()
{
	int n;
	int lst[100000];
	int ind = 0;
	cin >> n;
	if (n == 1)
	{
		cout << 1;
		return 0;
	}
	for (int i = 0; i < n; i++)
		cin >> lst[i];
	foor(i, n)
	{
		ans[ind]++;
		ans[i]++;
		if (lst[ind] > lst[i])
			ind = i;
	}
	int maxx = 0;
	int anss = -1;
	for (int i = 0; i < n; i++)
	{
		if (ans[i] > maxx)
		{
			maxx = ans[i];
			anss = i;
		}
	} 
	cout << anss + 1;
}	
