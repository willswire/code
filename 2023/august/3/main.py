class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) != 0:
            return []
        
        keyMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        if len(digits) == 1:
            return keyMap[digits]
        else:
            

    
Solution.letterCombinations(Solution, "23")