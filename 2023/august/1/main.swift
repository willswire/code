import Foundation

class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var count: Int = 1;
        for num in nums {
            for rest in nums.dropFirst(count) {
                if ((target - num - rest) == 0) {
                    return [nums.firstIndex(of: num)!, nums.lastIndex(of: rest)!]
                }
            }
            count += 1;
        }
        return []
    }
}
