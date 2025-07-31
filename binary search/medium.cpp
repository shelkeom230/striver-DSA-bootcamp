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

// gas stations -- better solution 
// usinng a priority queue (max heap)
long double gasStationBetter(vector<int> &arr,int k){
    int n=arr.size();
    vector<int> howManySt(n-1,0);
    priority_queue<pair<long double,int>> pq;

    // insert the initial distances into pq 
    for(int i=0;i<n;i++){
        pq.push({arr[i+1]-arr[i],i});
    }

    // pick and place each gas station 
    for(int i=1;i<=k;i++){
        // find the maximum section 
        // and place the gas station there
        auto tp=pq.top();
        pq.pop();
        int secIndx=tp.second;
        
        // place the current gas station at secIndx 
        howManySt[secIndx]++;

        // calculate the old section diff 
        long double initDiff=arr[secIndx+1]-arr[secIndx];
        long double newSecLength=initDiff/(long double)(howManySt[secIndx]+1);

        // push to new values in pq 
        pq.push({newSecLength,secIndx});
    }
    return pq.top().first; 
}

// gas station -- optimal 
long double gasStationOptimal(vector<int> &arr,int k){
    
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
    cout<<gasStationBetter(arr,k);

    return 0;
}
