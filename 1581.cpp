#include <iostream>

using namespace std;

int main(){
    int n;
    int count = 1;
    cin >> n;
    int x,xx;
    cin >> x;
    for(int i = 1; i < n; i++){
        cin >> xx;
        if(x == xx)
            count++;
        else{
            cout << count << " " << x << " ";
            count = 1;
        }
        x = xx;
    }

    cout << count << " " << x << " ";
}
