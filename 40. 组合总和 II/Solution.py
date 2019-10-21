class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        def backtrack(remain: int) -> None:
            for i in range(0 if path == [] else path[-1]+1, len(candidates)):
                if remain - candidates[i] > 0:
                    path.append(i)
                    backtrack(remain-candidates[i])
                elif remain - candidates[i] == 0:
                    e_res = list(map(lambda x: candidates[x], path+[i]))
                    if e_res not in res:
                        res.append(e_res)
            if not path == []: path.pop()
            return
        
        backtrack(target)
        return res