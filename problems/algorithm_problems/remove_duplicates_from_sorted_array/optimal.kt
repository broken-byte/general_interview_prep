

class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        if (nums.size <= 1) {
            return nums.size
        }
        var replacement_index = 1
        var buffer = nums[0]
        for (index in 1 until nums.size) {
            if (nums[index] != buffer) {
                buffer = nums[index]
                nums[replacement_index] = buffer
                replacement_index += 1
            }
        }
        return replacement_index
    }
}