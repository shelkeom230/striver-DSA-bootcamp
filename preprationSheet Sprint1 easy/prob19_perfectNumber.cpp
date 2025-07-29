// deterimine if a number is perfect number --> A perfect number is one which is equal to the sum of it's divisors
#include <bits/stdc++.h>
using namespace std;

#define int long long
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);

string checkPerfectNumber(int n){
    if(n<=1) return "true";

    vector<int> divisors;
    for(int i=1;i<=n-1;i++){
        if(n%i==0) divisors.push_back(i);
    }

    int sum=0;
    for(int val: divisors) {
        sum+=val;
    }
    if(sum==n) return "true";
    else return "false";
}
int32_t main()
{
    fastio;

    freopen("input.txt", "r", stdin);   // Read from input.txt
    freopen("output.txt", "w", stdout); // Write to output.txt
    int n;
    cin>>n;
    
    cout<<checkPerfectNumber(n);
    return 0;
}