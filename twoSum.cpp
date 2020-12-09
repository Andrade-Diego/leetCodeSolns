#include <map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> myMap; //key is a value needed to be found, value is index of it's mate to meet target
        vector<int> soln; //will contain index of solution
        for(int i = 0; i < nums.size(); i++){
            if(myMap.count(nums[i]) == 1){ // if a map key exists with the current i's value
                cout << myMap[nums[i]]<< ' ' << i << endl;

                //put indices in soln
                soln.push_back(i); 
                soln.push_back(myMap[nums[i]]);
                break;
            }
            myMap.insert(pair<int, int>(target - nums[i], i));// give map the number it needs to get to target and current index

        }
        return soln;
    }
};
