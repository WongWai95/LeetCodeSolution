class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        index = 0
        ret = 0
        
        for i in range(len(s)):
            if s[i] in hash_map:
                index = max(hash_map[s[i]], index)
            ret = max(ret, i-index+1)
            hash_map[s[i]] = i + 1
            
        return ret