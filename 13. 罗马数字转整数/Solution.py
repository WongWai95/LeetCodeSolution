class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'O': 0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman = s + 'O'
        num = 0
        
        for index in range(len(s)):
            if mapping[roman[index]] >= mapping[roman[index+1]]:
                num += mapping[roman[index]]
            else:
                num -= mapping[roman[index]]
                
        return num