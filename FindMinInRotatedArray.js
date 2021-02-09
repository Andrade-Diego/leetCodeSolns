/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let left = 0;
    let right = nums.length - 1;
    while (left < right){
        let mid = Math.floor((left + right) / 2);

        // if we found inflection point
        if (nums[mid - 1] > nums[mid]){
            return nums[mid];
        }
        if (nums[mid] > nums[mid + 1]){
            return nums[mid + 1];
        }

        // if the inflection point is to the left or
        // right of our current mid
        if (nums[mid] > nums[left]){
            left = mid;
            continue;
        }
        if (nums[mid] < nums[right]) {
            right = mid;
            continue;
        }
    }
    return nums[0];

};

let arr = [3,4,5,1,2];

console.log(`(TEST)\n\tTest Array: ${arr}\n\tMin Number: ${findMin(arr)}`);
