// print armstrong numbers within a given range 
#include <bits/stdc++.h>
using namespace std;

#define int long long
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);

bool isArmstrong(int n){
    int dup=n;
    int sum=0;
    while(n>0){
        int digit=n%10;
        sum+=(pow(digit,3));
        n/=10;
    }
    if(dup==sum) return true;
    else return false;
}

void printArmstrongInRange(int low,int high)
{
    for(int i=low;i<=high;i++){
        if(isArmstrong(i)) cout<<i<<" ";
    }
}
int32_t main()
{
    fastio;

    freopen("input.txt", "r", stdin);   // Read from input.txt
    freopen("output.txt", "w", stdout); // Write to output.txt

    int low,high;
    cin>>low>>high;
    printArmstrongInRange(low,high);
    return 0;
}