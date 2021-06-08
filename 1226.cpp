#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
using namespace std;

int main()
{
    string line1, line2;
    while (getline(cin, line1))
    {
        line2 = "";
        for (int i = 0; i < line1.length(); i++)
        {
            if (isalpha(line1[i]))
            {
                line2 = line1[i] + line2;
            }
            else
            {
                cout << line2;
                line2 = "";
                cout << line1[i];
            }  
        }
        cout << line2 << "\n";
    }
}
