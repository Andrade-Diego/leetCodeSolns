var findPeakElement = function(nums) {
    if (nums.length <= 1 || nums[0] > nums[1]){
        return 0;
    }
    if (nums[nums.length - 1] > nums[nums.length - 2]){
        return nums.length - 1;
    }

    for (let cur = 1; cur < nums.length - 1; cur ++){
        if ((nums[cur - 1] < nums[cur] && nums[cur] > nums[cur + 1])){
            return cur;
        }
    }
};

let arr = [3,4,5,1,2];

console.log(`(TEST)\n\tTest Array: ${arr}\n\tThere's a peak in the array at index: ${findPeakElement(arr)}`);
