#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
    int br[10024],i,m;
    double n,a;
    float sum;
    cin>>n>>a;
    sum=100/a;
    for(i=1;i<=10024;i++)
    {
        br[i]=0;
    }
    for(i=1;i<=a;i++)
    {
        cin>>m;
        br[m]++;
    }
    for(i=1;i<=n;i++)
    {

         printf("%.2lf",(br[i]*sum));
         cout<<"%"<<endl;
    }
    return 0;
}
