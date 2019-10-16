class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return ''
        
        pool = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        p = [0 for _ in range(len(digits))]
        result = pool[digits[0]]
        
        for i in range(1, len(digits)):
            result = ['%s%s' % (r, d) for r in result for d in pool[digits[i]]]
            
        return result