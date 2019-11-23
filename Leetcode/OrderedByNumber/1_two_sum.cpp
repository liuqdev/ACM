#include<iostream>
#include<vector>
#include<unordered_map>

using namespace std;

class Solution {
public:
    //查找表
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
        vector<int> res;
        for (int i = 0; i < nums.size(); ++i) {
            int complement=target-nums[i];

            if (hash.find(complement)!=hash.end()){
                //int res[2]={i, hash[complement]};
                res.push_back(hash[complement]);
                res.push_back(i);
                //return vector<int>(res,res+2);
                return res;
            }

            hash[nums[i]]=i;
        }
        throw invalid_argument("has no solution");
    }
};


int main(){
    vector<int> nums = {1, 1, 1, 1, 1, 1, 1};
    int target = 2;
    vector<int> res = Solution().twoSum(nums, target);

    for (int i=0; i<res.size(); i++) {
        cout << res[i] << endl;
    }
    return 0;
}