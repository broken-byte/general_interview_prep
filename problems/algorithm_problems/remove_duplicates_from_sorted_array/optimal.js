/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (nums.length <= 1) {
        return nums.length;
    }
    let replacement_index = 1;
    let buffer = nums[0];
    for (let index = 1; index < nums.length; index++) {
        if (nums[index] != buffer) {
            buffer = nums[index];
            nums[replacement_index] = buffer;
            replacement_index += 1;
        }
    }
    return replacement_index;
};