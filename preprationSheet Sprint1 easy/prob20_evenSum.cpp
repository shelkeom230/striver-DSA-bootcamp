// calculate sum of even numbers in a range 
#include <bits/stdc++.h>
using namespace std;

#define int long long
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);

    pair<int,int> findSum(int low,int high){
        int evensum=0,oddsum=0;
        for(int i=low;i<=high;i++){
            if(i%2==0) evensum+=i;
            else oddsum+=i;
        }
        return {evensum,oddsum};
    }
int32_t main()
{
    fastio;

    freopen("input.txt", "r", stdin);   // Read from input.txt
    freopen("output.txt", "w", stdout); // Write to output.txt
    int low,high;
    cin>>low>>high;

    pair<int,int> res = findSum(low,high);
    cout<<res.first<<" "<<res.second<<"\n";
    return 0;
}