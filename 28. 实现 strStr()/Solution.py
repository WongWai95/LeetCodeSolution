class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '': return 0
        index = -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                index = i
                break
        return index