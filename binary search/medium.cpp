#include <bits/stdc++.h>
using namespace std;

// Fast IO + File IO setup
void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    freopen("input.txt", "r", stdin);    // Read input from input.txt
    freopen("output.txt", "w", stdout);  // Write output to output.txt
}

// gas station -- brute force 
long double gasStationBrute(vector<int> &arr,int k){
    int n=arr.size();

    vector<int> howManySt(n-1,0);
    for(int i=1;i<=k;i++){
        long double maxValue=-1;
        int maxIndex=-1;

        for(int j=0;j<n-1;j++){
            long double diff=arr[j+1]-arr[j];
            long double sectionLength=diff/(long double)(howManySt[j]+1);
            if(sectionLength>maxValue){
                maxValue=sectionLength;
                maxIndex=j;
            }
        }
        howManySt[maxIndex]+=1;
    }

    // find the answer 
    long double maxAns=-1;

    for(int i=0;i<n-1;i++){
        long double diff=arr[i+1]-arr[i];
        long double sectionLength=diff/(long double)(howManySt[i]+1);
        maxAns=max(maxAns,sectionLength);
    }
    return maxAns;
}
int main() {
    setupIO();

    // write your code here 
    int n,k;
    cin>>n>>k;
    vector<int> arr(n);
    
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<gasStationBrute(arr,k);

    return 0;
}
