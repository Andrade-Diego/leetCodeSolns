var heapAlg = (nums, k, permutations) => {
    if (k == 1){
        permutations.unshift([...nums]);
        return;
    }
    heapAlg(nums, k - 1, permutations);

    for (let i = 0; i < k - 1; i++){
        if (k % 2 == 0){
            [nums[i], nums[k - 1]] = [nums[k - 1], nums[i]];


        } else {
            [nums[0], nums[k - 1]] = [nums[k - 1], nums[0]];
        }

        heapAlg(nums, k - 1, permutations);
    }
};

var permute = function(nums) {
    let permutations = [];
    heapAlg(nums, nums.length, permutations);
    return permutations;
};

let arr = [3,4,5,1,2];
let permutations = permute(arr);

console.log(`(TEST)\n\tTest Array: ${arr}\n\tPermutations:`);
for (let i = 0; i < permutations.length; i++){
  console.log(`\t\t${permutations[i]}`);
}
