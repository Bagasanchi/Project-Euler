#include<bits/stdc++.h>
using namespace std;
int main(){
    long long limit=4000000,sum=0;
    long long a=1,b=2;
    while (a <= limit) {
        if (a%2==0) sum+=a;
        long long next=a+b;
        a=b;
        b=next;
    }
    cout<<sum<<endl;
    return 0;
}