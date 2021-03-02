#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define all(v) v.begin(), v.end() 
#define sort(v) sort(ALL(v)) 
#define reverse(v) reverse(ALL(v)) 

typedef long long ll;
typedef vector<int> vi;

//start
int main()
{
	int n;
	bool can_pl[50000];
	bool can_mi[50000];
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		int k;
		scanf("%d", &k);
		if (k < 0)
			can_mi[-k] = 1;
		else
			can_pl[k] = 1;
	}
	
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		int k;
		scanf("%d", &k);
		if (10000 - k < 0)
		{
			if (can_mi[-(10000 - k)] == 1)
			{
				printf("%s", "YES");
				return 0;
			}
		}
		else
			if (can_pl[10000 - k] == 1)
			{
				printf("%s", "YES");
				return 0;
			}
	}
	printf("%s", "NO");
}