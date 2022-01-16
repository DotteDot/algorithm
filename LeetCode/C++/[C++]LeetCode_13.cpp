// 9 Palindrome Number.cpp

class Solution {
public:
    int romanToInt(string s) {
        map<char, int> symbol;
        symbol['I'] = 1;
        symbol['V'] = 5;
        symbol['X'] = 10;
        symbol['L'] = 50;
        symbol['C'] = 100;
        symbol['D'] = 500;
        symbol['M'] = 1000;
        
        if (s.length() == 0)
            return 0;
        
        else{
            int start = symbol[s[0]];
            int temp = symbol[s[0]];
            int i, result = 0;
            
            for(i = 1; i < s.length(); i++){
                
                std::cout << result << ' ' << start << ' ' << temp << std::endl;
                std::cout << symbol[s[i]] << std::endl;
                
                if (start == 0){
                    temp = symbol[s[i]];
                    start = symbol[s[i]];
                }
                else if (start < symbol[s[i]]){
                    result += symbol[s[i]] - temp;
                    start = 0;
                    temp = 0;
                }
                else if (start != symbol[s[i]]){
                    result += temp;
                    temp = symbol[s[i]];
                    start = symbol[s[i]];
                }
                else{
                    temp += symbol[s[i]];
                    start = symbol[s[i]];
                }
            }
            return temp + result;
        }
        return 0;
    }
};