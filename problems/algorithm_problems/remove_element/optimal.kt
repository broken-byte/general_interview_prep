

class Solution {
    fun removeElement(nums: IntArray, `val`: Int): Int {
        var left = 0;
        var right = nums.size - 1
        while (left <= right) {
            if (nums[left] == `val`) {
                nums[left] = nums[right].also { nums[right] = nums[left] }
                right--
            }
            else left++
        }
        return left
    }
}