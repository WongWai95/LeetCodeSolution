class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []

        def dfs(candidates, begin, target):
            if target == 0:
                res.append(path[:])

            for index in range(begin, size):
                residue = target - candidates[index]
                if residue < 0:
                    break
                path.append(candidates[index])
                dfs(candidates, index, residue)
                path.pop()
                
        dfs(candidates, 0, target)
        return res