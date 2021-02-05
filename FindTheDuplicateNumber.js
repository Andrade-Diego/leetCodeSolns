/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    let seen = new Set();
    for (let i = 0; i < nums.length; i++){
        if(seen.has(nums[i])){
            return nums[i];
        } else {
            seen.add(nums[i]);
        }
    }
    return false;
};
let arr = [1,2,3,4,5,6,7,8,3,9,10];
console.log(`(TEST)\n\tTest Array: ${arr}\n\tDuplicate Number: ${findDuplicate(arr)}`);
