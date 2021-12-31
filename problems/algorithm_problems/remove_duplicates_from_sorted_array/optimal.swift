

class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        if (nums.count <= 1) {
            return nums.count
        }
        var replacement_index = 1
        var buffer: Int = nums[0]
        for index in 1..<nums.count {
            if (nums[index] != buffer) {
                buffer = nums[index]
                nums[replacement_index] = buffer
                replacement_index+=1
            }
        }
        return replacement_index
    }
}