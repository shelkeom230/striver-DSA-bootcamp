// count the number of digits in a number 
// print all prime numbers less than n
#include <bits/stdc++.h>
using namespace std;

#define int long long
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);

int findSum(int n){
    int sum=0;
    while(n>0){
        int digit=n%10;
        sum+=digit;
        n/=10;
    }
    return sum;
}
int countDigits(int n){
    int cnt=0;
    while(n>0){
        cnt++;
        n/=10;
    }
    return cnt;
}
bool checkFunc(int n){
    int digitSum=findSum(n);
    int totalDigits=countDigits(n);
    if(pow(digitSum,totalDigits)==n) return true;
    else return false;
}
int32_t main()
{
    fastio;

    freopen("input.txt", "r", stdin);   // Read from input.txt
    freopen("output.txt", "w", stdout); // Write to output.txt

    int n;
    cin >> n;

    cout<<checkFunc(n);

    return 0;
}