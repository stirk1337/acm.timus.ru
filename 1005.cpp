#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;
int dp[2][1000005];
int w[25];
int main()
{
    int n, s = 0, g = 0, ans;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> w[i];
        s += w[i];
        g += w[i];
    }
    s /= 2;
    int col = 0;
    for (int i = 1; i <= n; i++) {
        col = 1 - col;
        for (int j = 0; j <= s; j++) {
            dp[1 - col][j] = dp[col][j];
            if (w[i] <= j)
                dp[1 - col][j] = max(dp[col][j - w[i]] + w[i], dp[1 - col][j]);
        }
        ans = dp[1 - col][s];
    }

    cout << abs(g-ans-ans);
    
}