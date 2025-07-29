// find fib value at n
#include <bits/stdc++.h>
using namespace std;

#define int long long
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);

    int findFib(int n){
        if(n<=1) return n;
        
        return findFib(n-1)+findFib(n-2);
    }
    // iterative findfib 
    int findFibIter(int n){
        if(n<=1) return n;

        int val=0;
        int first,second;
        first=0,second=1;
        for(int i=2;i<=n;i++){
            val=first+second;
            first=second;
            second=val;
        }
        return val;
    }
int32_t main()
{
    fastio;

    freopen("input.txt", "r", stdin);   // Read from input.txt
    freopen("output.txt", "w", stdout); // Write to output.txt
    int n;
    cin>>n;

    cout<<findFibIter(n);
    return 0;
}