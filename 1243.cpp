#include <iostream>
#include <string>
using namespace std;
int main()
{
    string n;
    cin >> n;
    int ans = 0;
    for (int i = 0; i < n.size(); i++)
    {
        ans = (10 * ans + (n[i] - '0'))  % 7;
    }
    cout << ans;
}
