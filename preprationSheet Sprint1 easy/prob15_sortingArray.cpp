#include <bits/stdc++.h>
using namespace std;

#define int long long
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);

// bubble sort
vector<int> bubbleSort(vector<int> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
    return arr;
}

// selection sort
vector<int> selectionSort(vector<int> &arr)
{
    int n = arr.size();

    for (int i = 0; i < n; i++)
    {
        int minele = i;
        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[minele])
                minele = j;
        }
        swap(arr[i], arr[minele]);
    }
    return arr;
}

// insertion sort
vector<int> insertionSort(vector<int> &arr)
{
    int n = arr.size();

    for (int i = 0; i < n; i++)
    {
        int j = i;
        while (n > 0 && arr[j - 1] > arr[j])
        {
            int temp = arr[j - 1];
            arr[j - 1] = arr[j];
            arr[j] = temp;
            j -= 1;
        }
    }
    return arr;
}

// merge function
void merge(vector<int> &arr, int low, int mid, int high)
{
    int left, right;
    left = low, right = high;
    vector<int> temp;
    while (left <= mid && right <= high)
    {
        if (arr[left] <= arr[right])
        {
            temp.push_back(arr[left]);
            left++;
        }
        else
        {
            temp.push_back(arr[right]);
            right++;
        }
    }

    // append remaing elements
    while (left <= mid)
    {
        temp.push_back(arr[left]);
        left++;
    }
    while (right <= high)
    {
        temp.push_back(arr[right]);
        right++;
    }

    // copy back temp to original array
    for (int i = 0; i < temp.size(); i++)
    {
        arr[i + low] = temp[i];
    }
}
// merge sort
void mergeSort(vector<int> &arr, int low, int high)
{
    if (low >= high)
        return;

    int mid = (low + high) / 2;

    mergeSort(arr, low, mid);
    mergeSort(arr, mid + 1, high);
    merge(arr, low, mid, high);
}
// pivotIndex function
int pivotIndex(vector<int>& arr,int low,int high){
    int i,j,pivot;
    pivot=arr[low];
    i=low+1,j=high;

    while(i<=j){

        while(i<=high && arr[i]<=pivot) i++;
        while(j>=low && arr[j]>pivot) j--;

        if(i<j) swap(arr[i],arr[j]);
    }

    // place pivot at correct index 
    swap(arr[low],arr[j]);
    return j;
}
    // quick sort
    void quickSort(vector<int> & arr, int low, int high)
    {
        if (low >= high)
            return;

        int pivot = pivotIndex(arr, low, high);

        quickSort(arr, low, pivot - 1);
        quickSort(arr, pivot + 1, high);
    }

    int32_t main()
    {
        fastio;

        freopen("input.txt", "r", stdin);   // Read from input.txt
        freopen("output.txt", "w", stdout); // Write to output.txt
        int n;
        cin >> n;

        vector<int> v;
        for (int i = 0; i < n; i++)
        {
            int x;
            cin >> x;
            v.push_back(x);
        }

        quickSort(v, 0, v.size()-1);
        for (int val : v)
        {
            cout << val << " ";
        }

        return 0;
    }