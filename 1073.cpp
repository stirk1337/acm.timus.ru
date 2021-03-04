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
int dp[60001];
int main()
{
    int n;
    scanf("%d", &n);
    dp[0] = 0;
    for (int i = 1; i <= n; i++)
    {
        dp[i] = dp[i - 1] + 1;
        for (int j = 1; j * j <= i; j++)
            if (i >= j * j)
                dp[i] = min(dp[i], 1 + dp[i - j * j]);
            else
                break;
    }
    printf("%d\n", dp[n]);
}