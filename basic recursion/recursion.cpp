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
// print one infinite times 
void printOneInfinite(){
    cout<<"1"<<endl;
    printOneInfinite();
}

// print upto a specified value n 
void printUptoN(int cnt,int n){
    if(cnt>n){
        return;
    }
    cout<<cnt<<" ";
    return printUptoN(cnt+1,n);
}

// print even numbers 
int k=0;
void printEvenUptoN(){
    if(k>10)
    return;

    cout<<k<<" ";
    k+=2;
    return printEvenUptoN();

}
// print odd numbers 
int odd=1;
void printOdduptoN(){
    if(odd>10) return;
    cout<<odd<<" ";
    odd+=2;
    return printOdduptoN();
}
// print your name n times 
void printNameNTimes(int cnt,int n){
    if(cnt>n) return;
    cout<<"Omkar CP2005"<<endl;
    return printNameNTimes(cnt+1,n);
}
// print in range i to n 
void printInRange(int i,int n){
    if(i>n) return;
    cout<<i<<" ";
    return printInRange(i+1,n);
}
// print even numbers from i to n 
void printEvenInRange(int i,int n){
    if(i>n) return;
    if(i&1==0) cout<<i<<" ";
    return printEvenInRange(i+1,n);
}
// print from N to 1 
void printInReverse(int n){
    if(n<1) return;
    cout<<n<<" ";
    return printInReverse(n-1);
}
int main() {
    setupIO();

    // write your code here 
    int n;
    cin>>n;
    printInReverse(n);
    return 0;
}
