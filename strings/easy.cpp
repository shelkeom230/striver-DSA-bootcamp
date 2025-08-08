#include <bits/stdc++.h>
using namespace std;

// Fast IO + File redirection for local testing
void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
}

// Typedefs
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;

// Debugging (only enabled locally)
#ifndef ONLINE_JUDGE
#define debug(x) cerr << #x << " = "; _print(x); cerr << endl;
#else
#define debug(x)
#endif

// Debug printing helpers
void _print(int x)      { cerr << x; }
void _print(ll x)       { cerr << x; }
void _print(string x)   { cerr << x; }
void _print(char x)     { cerr << x; }
void _print(double x)   { cerr << x; }
template<class T> void _print(vector<T> v) { cerr << "[ "; for (T i : v) { _print(i); cerr << " ";Firebase: Error (auth/operation-not-allowed).
    _FirebaseError errors.ts:85
    create errors.ts:123
    createErrorInternal assert.ts:146
    _createError assert.ts:83
    sendToConsumer auth_event_manager.ts:95
    onEvent auth_event_manager.ts:68
    onEvent auth_event_manager.ts:65
    initAndGetManager popup_redirect.ts:139
    Rm cb=gapi.loaded_0:194
    Sm cb=gapi.loaded_0:194
    gl cb=gapi.loaded_0:173
    pl cb=gapi.loaded_0:173
    Kk cb=gapi.loaded_0:174
    FH cb=gapi.loaded_0:167
    Ne cb=gapi.loaded_0:92
    Oe cb=gapi.loaded_0:92
    Qk cb=gapi.loaded_0:166
    <anonymous> cb=gapi.loaded_0:177
    Ga api.js:21
    Fa api.js:24
    Ga api.js:21
    la api.js:23
    B api.js:23
    v api.js:24
    S api.js:24
    <anonymous> cb=gapi.loaded_0:1 } cerr << "]"; }
template<class T, class V> void _print(pair<T, V> p) { cerr << "{"; _print(p.first); cerr << ", "; _print(p.second); cerr << "}"; }

// remove outer parentheses -- brute force 
string removeParenBruteForce(string s){
    int n=s.size();
    vector<string> ans;
    int openCnt=0,closeCnt=0,last=0;
    for(int i=0;i<n;i++){
        if(s[i]=='(') openCnt++;
        else closeCnt++;

        if(openCnt==closeCnt) {
            ans.push_back(s.substr(last,i-last+1));
            last=i+1;
        }
    }

    // remove the outer symbols 
    for(string &str: ans){
        if(str.length()>=2 && str.front()=='(' && str.back()==')')
        str=str.substr(1,str.length()-2);
    }
    string finalResult="";
    for(const string &part:ans){
        finalResult+=part;
    }
    return finalResult;
}

// remove outer parentheses -- stack based approach 
string removeParenStackBased(string s){
    stack<char> st;
    string ans;
    for(char ch:s){
        if(ch=='('){
            if(!st.empty()) ans+=ch;
            st.push(ch);
        }else{ // ch==')'
            st.pop();
            if(!st.empty()) ans+=ch;
        }
    }
    return ans;
} 
// remove outer parentheses -- optimal 
string removeParenOptimal(string s){
    int depth=0;
    string ans="";
    for(int i=0;i<s.size();i++){
       if(s[i]=='('){
        if(depth>0) ans+=s[i];
        depth++;
       }
       if(s[i]==')'){
        depth--;
        if(depth>0) ans+=s[i];
       }
    }
    return ans;
}

// reverse a word 
void revWord(string &word){
    int left=0,right=word.size()-1;
    while(left<right){
        char temp=word[left];
        word[left]=word[right];
        word[right]=temp;
        left+=1;
        right-=1;
    }
    
}
// rev each word in a sentence -- brute force 
string revSentence(string &sen){
    string words[100];
    string temp="";
    string ans="";
    int wordsCnt=0;
    for(int i=0;i<sen.size();i++){
        if(sen[i]==' ' || sen[i]=='\0'){
            words[wordsCnt++]=temp;
        }else{
            temp+=sen[i];
        }
    }

    // ["omkar","shelke"]
    for(int j=wordsCnt-1;j>=0;--j){
        ans+=words[j];
        ans+=' ';
    }
    return ans;
}
int main() {
    setupIO();
    string s;
    cin>>s;
    revWord(s);
    cout<<s;
    return 0;
}
