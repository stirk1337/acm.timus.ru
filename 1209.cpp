#include <iostream>
#include <set>

using namespace std;

int main() {
    int n; cin >> n;
    set<unsigned int> v;
    unsigned int a = 1, c = 0;
    while(a <= (1<<31)) {
        v.insert( a );
        a += c++;
    }
    for(int i = 0; i < n; ++i) {
        cin >> a;
        if(*v.find(a) == v.size()) {
            cout << 0 << ' ';
        } else {
            cout << 1 << ' ';
        }
    }
}
