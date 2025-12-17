#include <iostream>
using namespace std;
int main()
{
    // int a,b;
    // cout<<"Enter the value of a :"<<endl;
    // cin>>a;
    // cout<<"Enter the value of b :"<<endl;
    // cin>>b;
    // if(a>b)
    // {
    //     cout<<"The larger value is : "<<a<<endl;
    // }
    // else
    // {
    //     cout<<"The larger value is : "<<b<<endl;
    // }
    int a[5] = {10,20,30,40,50};
    int large=a[0];
    for(int i=0;i<5;i++)
    {
        if(a[i]>large)
        {
            large=a[i];
        }
    }
    cout<<"The larger value is : "<<large<<endl;
    return 0;
}
