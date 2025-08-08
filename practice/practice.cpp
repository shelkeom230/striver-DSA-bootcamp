#include <bits/stdc++.h>
using namespace std;

float getPerc(int marks){
    float perc=(marks*100)/500.0;
    return perc;
}
int main(){
    int marks;
    cout<<"enter your marks";
    cin>>marks;

    cout<<getPerc(marks);
    return 0;
}