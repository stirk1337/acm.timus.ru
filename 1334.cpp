#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define ALL(v) v.begin(), v.end() 
#define sort(v) sort(ALL(v)) 
#define reverse(v) reverse(ALL(v)) 
#define for(i, a, n) for(int i = a; i < n; i++)

typedef long long ll;
typedef vector<int> vi;

//start
int deck[8][8];
int main()
{
	int y, x;
	char turnx;
	for (k, 1, 33)
	{
		scanf("\n%c%d", &turnx, &y); y--;
		x = turnx - 'a';
		if (k % 2 == 0)
			deck[y][x] = 2; //black
		else
			deck[y][x] = 1; //white

		/*for (i, 0, 8)
		{
			for (j, 0, 8)
				cout << deck[i][j] << " ";
			cout << endl;
		}*/
		for (i, 1, 7)
			for (j, 1, 7)
			{
				if (deck[i][j] == 2)
				{
					if ((deck[i - 1][j - 1] == 1 && deck[i + 1][j + 1] == 0) || (deck[i - 1][j - 1] == 0 && deck[i + 1][j + 1] == 1) || (deck[i - 1][j + 1] == 1 && deck[i + 1][j - 1] == 0) || (deck[i - 1][j + 1] == 0 && deck[i + 1][j - 1] == 1))
					{
						printf("%d", k);
						return 0;
					}
				}
				if (deck[i][j] == 1)
				{
					if((deck[i - 1][j - 1] == 2 && deck[i + 1][j + 1] == 0) || (deck[i - 1][j - 1] == 0 && deck[i + 1][j + 1] == 2) || (deck[i - 1][j + 1] == 2 && deck[i + 1][j - 1] == 0) || (deck[i - 1][j + 1] == 0 && deck[i + 1][j - 1] == 2))
					{
						printf("%d", k);
						return 0;
					}
				}
			}
	}
	printf("%s", "Draw");
}
