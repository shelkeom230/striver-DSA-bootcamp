// print all prime numbers less than n
#include <bits/stdc++.h>
using namespace std;

#define int long long
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);
bool checkPrime(int n)
{
    if (n <= 1)
        return false;
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}
void printPrime(int n)
{
    for (int i = 2; i <= n; i++)
    {
        if (checkPrime(i))
        {
            cout << i << " ";
        }
    }
}
int32_t main()
{
    fastio;

    freopen("input.txt", "r", stdin);   // Read from input.txt
    freopen("output.txt", "w", stdout); // Write to output.txt

    int n;
    cin >> n;

    printPrime(n);

    return 0;
}