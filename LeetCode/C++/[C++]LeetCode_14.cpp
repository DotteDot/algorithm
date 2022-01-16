// 14 Longest Common Prefix.cpp

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        int flag = 0;
        string result = "";
        
        for (int j = 0; j < strs[0].length(); j++){
            char init_chr;
            if (flag == 1)
                break;
            
            for (int i = 0; i < n; i++){
                init_chr = strs[0][j];
                
                if (strs[i].length() < j){
                    flag = 1;
                    break;
                }
                else{
                    if(strs[i][j] == init_chr)
                        continue;
                    else{
                        flag = 1;
                        break;
                    }
                }
            }
            if (flag == 0)
                result += init_chr;
        }
        return result;
    }
};