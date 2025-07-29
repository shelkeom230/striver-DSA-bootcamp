// print all prime numbers in given range
#include <bits/stdc++.h>
using namespace std;

#define int long long
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);

bool checkPrime(int n){
    int cnt=0;
    for(int i=1;i<=(int)sqrt(n);i++){
        if(n%i==0){
            cnt++;
            if((n/i)!=i) cnt++;
        }
    }
    if(cnt==2) return true;
    else return false;
}
void printPrimeInRange(int low,int high){
    for(int i=low;i<=high;i++){
        if(checkPrime(i)) cout<<i<<" ";
    }
}
int32_t main()
{
    fastio;

    freopen("input.txt", "r", stdin);   // Read from input.txt
    freopen("output.txt", "w", stdout); // Write to output.txt
    int low,high;
    cin>>low>>high;
    printPrimeInRange(low,high);
    return 0;
}