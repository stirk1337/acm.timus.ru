#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

const int maxn = 150005;
struct Node
{
    int index;
    int ID;
    int mount;
}node[maxn];

int N;

bool cmp(Node &a, Node &b)
{
    if (a.mount != b.mount)
    {
        return a.mount > b.mount;
    }
    else
    {
        return a.index < b.index;
    }
}

int main()
{
    scanf("%d", &N);
    for (int i=0; i<N; i++)
    {
        scanf("%d%d", &node[i].ID, &node[i].mount);
        node[i].index = i;
    }

    sort(node, node + N, cmp);

    for (int i=0; i<N; i++)
    {
        printf("%d %d\n", node[i].ID, node[i].mount);
    }
    return 0;
}