class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        p = [[False for _ in range(length)] for _ in range(length)]
        max_len = 0
        result = ''
        
        for span in range(1, length+1):
            for start in range(length):
                end = start + span - 1
                if end > length - 1:
                    break
                p[start][end] = span==1 or (span==2 and s[start]==s[end]) or (p[start+1][end-1]==True and s[start]==s[end])
                if p[start][end]==True:
                    if span > max_len:
                        max_len = span
                        result = s[start:end+1]
                        
        return result