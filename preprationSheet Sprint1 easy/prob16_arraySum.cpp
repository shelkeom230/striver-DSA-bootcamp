// find sum of elements in an array
#include <bits/stdc++.h>
using namespace std;

#define int long long
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);

int arraySum(vector<int> arr)
{
    int sum=0;
    for(int i=0;i<arr.size();i++){
        sum+=arr[i];
    }
    return sum;
}
// shortcut way with formula 
int arraySum2(vector<int>& arr){
    int n=arr.size();
    int totalSum=(n*(n+1))/2;
    return totalSum;
}
int32_t main()
{
    fastio;

    freopen("input.txt", "r", stdin);   // Read from input.txt
    freopen("output.txt", "w", stdout); // Write to output.txt

    int n;
    cin>>n;
    vector<int> arr;
    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        arr.push_back(x);
    }

    cout<<arraySum2(arr);
    return 0;
}