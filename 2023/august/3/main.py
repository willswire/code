KEYMAP = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return KEYMAP[digits]
        else:
            rootCombinations = self.letterCombinations(digits[:-1])
            finalCombinations = []
            for combination in rootCombinations:
                for letter in KEYMAP[digits[-1]]:
                    finalCombinations.append(combination + letter)
            return finalCombinations