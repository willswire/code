class Solution {
    func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
        for numbers in matrix {
            if numbers.contains(target) {
                return true
            }
        }
        return false;
    }
}