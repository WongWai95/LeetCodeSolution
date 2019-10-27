class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        s = s.rstrip()
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                return count
            else:
                count += 1
        return count