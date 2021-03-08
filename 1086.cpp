#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define all(v) v.begin(), v.end() 
#define sort(v) sort(ALL(v)) 
#define reverse(v) reverse(ALL(v)) 
#define foor(i,n) for(int i = 0; i < n; i++)

typedef long long ll;
typedef vector<int> vi;

//start
bool sieve[170000];
int primes[15005];
int k, q;
int max_prime = 0;
vi ans;
vi needtocheck;
int iter = 0;
int main()
{
	for (int i = 2; i <= 170000; i++)
	{
		if (sieve[i] == 0)
		{
			ans.pb(i);
			for (int j = i; (ll)j * i <= 170000; j++) {
				sieve[i * j] = 1;
			}
		}
	}
	
	scanf("%d", &k);
	for (int i = 0; i < k; i++)
	{
		scanf("%d", &q);
		printf("%d\n", ans[q - 1]);
	}

}