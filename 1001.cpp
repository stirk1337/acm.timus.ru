#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define ALL(v) v.begin(), v.end() 
#define sort(v) sort(ALL(v)) 
#define reverse(v) reverse(ALL(v)) 
#define foor(i,n) for(int i = 0; i < n; i++)

typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vll;

//start
int main()
{
	ll a;
	vll ans;
	while (scanf(" %lld", &a) != EOF)
		ans.pb(a);
	for (int i = ans.size() - 1; i >= 0; i--)
		printf("%.4f\n", sqrt(ans[i]));


}