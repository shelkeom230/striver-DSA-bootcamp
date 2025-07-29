// generate multipliction table of number n upto k
#include <bits/stdc++.h>
using namespace std;

#define int long long
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);

void mulTable(int n,int k){
    for(int i=1;i<=k;i++){
        cout<<n<<"*"<<i<<" = "<<(n*i)<<"\n";
    }
}
int32_t main()
{
    fastio;

    freopen("input.txt", "r", stdin);   // Read from input.txt
    freopen("output.txt", "w", stdout); // Write to output.txt

    int n,k;
    cin>>n>>k;
    mulTable(n,k);
    return 0;
}