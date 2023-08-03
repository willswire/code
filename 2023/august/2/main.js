/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const xString = x.toString();
    const xStringRev = xString.split("").reverse().join("");
    return (xString === xStringRev)
};