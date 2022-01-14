// 9 Palindrome Number.cpp

class Solution {
public:
    bool isPalindrome(int x) {
        string s = to_string(x);
        string s_x = to_string(x);
        reverse(s.begin(), s.end());
        
        if (s == s_x){
            return true;
        }
        else{
            return false;
        }
    }
};