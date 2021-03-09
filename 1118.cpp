#include <bits/stdc++.h>

using namespace std;

bool prime[1000010];

double sum_allDivisors(int n){
    long long sum = 0;
    for(int i = 1; i * i <= n; i++){
        if(n % i == 0)
            if(n/i == i)
                sum += i;
            else
                sum += i + n/i;
    }
    return sum;
}

int sieve(int n){
    for(long long i = 2; i <= n; i++){
        if(!prime[i])
            //if(i * i <= n)
                for(long long j = i * i; j <= n; j+= i)
                    prime[j] = 1;
    }
}


int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//freopen("input.txt", "r", stdin);
    sieve(1000000);
	int a, b, ans = 0;
    double minimum = 1e9;
    cin >> a >> b;

    if(a == 1){
        cout << 1;
        return 0;
    }

    for(int i = b; i >= a; i--){
        double tmp = sum_allDivisors(i)/i;
        if(tmp < minimum){
            minimum = tmp;
            ans = i;
        }
        if(!prime[i])
            break;
    }

    cout << ans;
}