#include <bits/stdc++.h>
using namespace std;

void fast_io() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    // File redirection
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
}
// max subarray sum, most brute force appraoch , 0(N^3), 0(1)
int maxSubarraySum_brute(vector<int>& arr, int n) {
    int maxSum = INT_MIN;

    for(int i = 0; i < n; i++) {
        for(int j = i; j < n; j++) {
            int sum = 0;

            for(int k = i; k <= j; k++) {
                sum += arr[k];
            }
            maxSum = max(maxSum, sum);
        }
    }
    return maxSum;
}
// maximum subarray sum , quite better approach 0(N^2)
int generateSubarrays(vector<int>& arr) {
    if(arr.size() == 1) return arr[0];
    int maxSum = 0;
    for(int i = 0; i < arr.size(); i++) {
        int sum = 0;
        for(int j = i; j < arr.size(); j++) {
            sum += arr[j];
            maxSum = max(maxSum, sum);
        }
    }
    return maxSum;
}

// max subarray sum , most optimal approach, kadane's algorithm
int maxSubarray_optimal(vector<int>& arr) {
    int sum = 0, maxSum = INT_MIN;

    for(int i = 0; i < arr.size(); i++) {
        sum += arr[i];

        if(sum > maxSum)
            maxSum = max(maxSum, sum);

        if(sum < 0) sum = 0;
    }
    return maxSum;
}

// follow up, return the indexes of subarray with gives the max sum
int maxSubarraySum_indexes(vector<int>& arr) {
    int sum = 0, maxSum = INT_MIN;
    int start = -1, ansStart = -1, ansEnd = -1;

    for(int i = 0; i < arr.size(); i++) {

        if(sum == 0) start = i;
        sum += arr[i];

        if(sum > maxSum) {
            maxSum = sum;
            ansStart = start;
            ansEnd = i;
        }

        if(sum < 0)
            sum = 0;
    }
    // print the subarray
    cout << "[ ";
    for(int i = ansStart; i <= ansEnd; i++) {
        cout << arr[i] << " ";
    }
    cout << "]" << endl;

    if(maxSum < 0) maxSum = 0;

    return maxSum;
}
// stock buy and sell , brute force , 0(N^2)
int stockBuySell(vector<int>& arr) {
    int n = arr.size();
    int maxProfit = INT_MIN;
    for(int i = 0; i < n - 1; i++) {
        for(int j = i + 1; j < n; j++) {
            if(arr[j]>arr[i])
            maxProfit=max(maxProfit,arr[j]-arr[i]);
        }
    }
    return maxProfit;
}

// stock buy and sell , optimal approach, 2 ptrs, 0(N)
int stockBuySell_optinal(vector<int>& arr){
    int n=arr.size();
    int maxProfit=0;
    int minPrice=arr[0];
    
    for(int i=0;i<n;i++){
        int cost=arr[i]-minPrice;
        maxProfit=max(maxProfit,cost);
        minPrice=min(minPrice,arr[i]);
    }
    return maxProfit;
    }
int main() {
    fast_io();

    // Example: read and echo input
    int n;
    cin >> n;

    vector<int> arr(n);
    for(auto &x : arr) cin >> x;
    cout << stockBuySell_optinal(arr);
    return 0;
}
