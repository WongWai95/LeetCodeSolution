class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if s == '' or words == []: return []
        hash_map = {}
        res = []
        for e in words:
            if e not in hash_map:
                hash_map[e] = 1
            else:
                hash_map[e] += 1
        
        for left in range(len(s)-len(words)*len(words[0])+1):
            temp_map = hash_map.copy()
            for right in range(left, left+len(words)*len(words[0]), len(words[0])):
                if s[right:right+len(words[0])] in temp_map and temp_map[s[right:right+len(words[0])]] != 0:
                    temp_map[s[right:right+len(words[0])]] -= 1
                else:
                    break
                if right == left + len(words) * len(words[0]) - len(words[0]):
                    res.append(left)
        return res