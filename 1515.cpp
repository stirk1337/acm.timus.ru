#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define all(v) v.begin(), v.end() 
#define sort(v) sort(all(v)) 
#define reverse(v) reverse(all(v)) 

typedef long long ll;
typedef vector<int> vi;

//start
int main()
{
	int n;
	int a[105];
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> a[i];
	
	int ans = 0;
	for (int i = 0; i < n; i++)
		if (a[i] > ans + 1)
			break;
		else
			ans += a[i];
	cout << ans + 1;


}
