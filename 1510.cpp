#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n, g;
    vector <int> a;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> g;
        a.push_back(g);
    }
    sort(a.begin(), a.end());
    cout << a[n / 2];
}
