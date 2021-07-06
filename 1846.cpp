#include <bits/stdc++.h>

using namespace std;

const int T = pow(2,17);
map<int, vector<int>> numbers;
int rsq[500000];

int gcd (int a, int b) {
	if (b == 0)
		return a;
	else
		return gcd (b, a % b);
}

void build(){
    for(int i = 0; i < 100005; i++)
        rsq[T+i] = -1;
    for(int i = T-1; i > 0; i--)
        rsq[i] = -1;
}

void change_elem(int j, int x){
    rsq[T+j] = x;
    for(int i = (T+j)/2; i > 0; i/=2)
        if(rsq[i*2] != -1 && rsq[i*2+1] != -1)
            rsq[i] = gcd(rsq[i*2], rsq[i*2+1]);
        else if(rsq[i*2] == -1)
            rsq[i] = rsq[i*2+1];
        else
            rsq[i] = rsq[i*2];
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//freopen("input.txt", "r", stdin);
    int t, n, index = 0;
    build();
    string inp;
    cin >> t;
    while(t--){
        cin >> inp >> n;
        if(inp == "+"){
            numbers[n].push_back(index);
            index++;
            change_elem(index-1, n);
            cout << rsq[1] << "\n";
        }
        else{
            int id = numbers[n].back();
            numbers[n].pop_back();
            change_elem(id, -1);
            if(rsq[1] == -1)
                cout << 1 << "\n";
            else
                cout << rsq[1] << "\n";
        }



    }

    //for(int i = 0;i < 100; i++)
    //    cout << rsq[i] << " ";
}
