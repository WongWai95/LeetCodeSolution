class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        res = []
        for e in strs:
            encode = str(sorted(e))
            if not encode in hash_map:
                res.append([])
                hash_map[encode] = len(res) - 1
            res[hash_map[encode]].append(e)
        return res