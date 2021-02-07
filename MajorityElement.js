var majorityElement = function(nums) {
    let maj = Math.floor(nums.length / 2);
    let count = {};
    for (let i = 0; i < nums.length; i ++){
        if (nums[i] in count){
            count[nums[i]] ++;
        } else {
            count[nums[i]] = 1;
        }
        if (count[nums[i]] > maj){
            return nums[i];
        }
    }
};
arr = [1,1,2,2,2,1,1]
console.log(`(TEST)\n\tTest Array: ${arr}\n\tMajority Number: ${majorityElement(arr)}`);
