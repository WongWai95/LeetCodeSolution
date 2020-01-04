class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        simplified = ''
        for e in s:
            if '0' <= e <= '9' or 'a' <= e <= 'z':
                simplified += e
        print(simplified)
        return simplified == simplified[::-1]