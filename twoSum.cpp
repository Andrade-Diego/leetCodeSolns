#include <map>
#include <vector>
#include <iostream>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    //key is a value needed to be found, value is index of it's mate to meet target
    map<int, int> myMap;

    //will contain index of solution
    vector<int> soln;

    //loop through nums 
    for(int i = 0; i < nums.size(); i++){

        // if a map key exists with the current i's value
        if(myMap.count(nums[i]) == 1){

            //put indices in soln
            soln.push_back(i); 
            soln.push_back(myMap[nums[i]]);

            //end early
            break;
        }

        // give map the number it needs to get to target and current index
        myMap.insert(pair<int, int>(target - nums[i], i));

    }
    return soln;
}

int main(){
    // This is a testcase
    cout <<"(TEST)\n\tList = {2, 7, 11, 15}\n\tTarget = 9" << endl;
    vector<int> nums{2,7,11,15};
    int target = 9;
    vector<int> result = twoSum(nums, target);
    cout << "\tResult = [" << result[0] << ", " << result[1] << "]" << endl;
}