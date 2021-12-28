

class Solution {
    func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
        var start = 0
        var end = nums.count - 1
        while (start <= end) {
            if (nums[start] == val) {
                nums.swapAt(start, end)
                end = end - 1
            } else {
                start = start + 1
            }
        }
        return start
    }
}