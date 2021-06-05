#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
    int n, bl, md, minsum = 0, maxsum = 0, max = 10000, ms = 0;
    string nothing;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> nothing >> bl;
        if (bl != 0)
        {
            cin >> md;
            max = md;
            maxsum += md;
            minsum += md *(ms+1);
            ms = 0;
        }
        else
        {
            maxsum += max;
            ms += 1;
        }
    }
    minsum += ms;
    if ((10000 >= minsum) && (10000 <= maxsum))
    {
        cout << "YES";
    }
    else {
        cout << "NO" << "\n";
    }
    //cout << maxsum << " " << minsum;
}
