/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    const first = nums[0];
    const last = nums[nums.length - 1];
    
    var i = 0;
    if (target == first) {
        return 0;
    } else if (target == last) {
        return nums.length - 1;
    } else if (target > first) {
        while (target > nums[i]) {
            i++;
        }
    } else if (target < last) {
        i = nums.length - 1;
        while (target < nums[i]) {
            i--;
        }
    }
    
    if (nums[i] == target) {
        return i;
    } else {
        return -1;
    }
};

console.log(search([4,5,6,7,0,1,2], 0) == 4)
console.log(search([4,5,6,7,0,1,2], 3) == -1)
console.log(search([1,3,5], 3) == 1)