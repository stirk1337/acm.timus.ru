#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <utility>
#include <queue>
#include <deque>
#include <string>
#include <cmath>
#include <list>
#include <stack>
#include <cstdlib>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//freopen("input.txt", "r", stdin);
	int m;
    vector<int> a;
    cin >> m;
    int much = 0;
    int n;
    while(cin >> n){
        if (n == -1)
            break;
        a.push_back(n);
    }
    int count[200005];
    set<int> now;
    for(int i = 0; i < m; i++){
        count[a[i]]++;
        now.insert(a[i]);
    }

    auto maximum = now.end();
    maximum--;
    cout << *maximum << endl;
    for(size_t i = m; i < a.size(); i++){
        count[a[i-m]]--;
        if (count[a[i-m]] == 0)
            now.erase(a[i-m]);
        count[a[i]]++;
        now.insert(a[i]);
        maximum = now.end();
        maximum--;
        cout << *maximum << endl;
    }
}
