#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,s=0;
    cin>>n;
    for(int i=0;i<n;i++){
        if(i%5==0 || i%3==0) s+=i;
    }
    cout<<s;
    return 0;
}

// If we list all the natural numbers below 10 that are multiples of 3 or 5 we get 3,5,6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000