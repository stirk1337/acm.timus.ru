#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define ALL(v) v.begin(), v.end() 
#define sort(v) sort(ALL(v)) 
#define reverse(v) reverse(ALL(v)) 
#define foor(i,n) for(int i = 0; i < n; i++)

typedef long long ll;
typedef vector<int> vi;

ll l[400005];
ll ps[400005];
int main()
{
	ll n;
	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> l[i];
	ps[0] = l[0];
	for (int i = 1; i <= n; i++)
	{
		ps[i] = ps[i - 1] + l[i];
	}
	ll q;
	cin >> q;
	foor(i, q)
	{
		int a, b;
		cin >> a >> b;
		cout << ps[b] - ps[a - 1] << "\n";
	}
}
