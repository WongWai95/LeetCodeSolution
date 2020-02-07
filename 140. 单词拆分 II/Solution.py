class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        hash_set = set(wordDict)
        mem = {}
        def _iter(begin: int) -> list:
            # print('iter begin:', begin)
            res = []
            if begin == len(s): return ['']
            for i in range(begin+1, len(s)+1):
                # print('loop begin:', begin, '->', i)
                if s[begin:i] in hash_set:
                    # print('catch word:', s[begin:i])
                    if i in mem:
                        # print('use mem:', i)
                        for e in mem[i]:
                            res.append(s[begin:i] + ' ' + e)
                    else:
                        # print('use _iter:', i)
                        for e in _iter(i):
                            res.append(s[begin:i] + ' ' + e)
                    # print('res for one loop:', res)
            mem[begin] = res
            # print('res for one iter:', res)
            return res
        ret = _iter(0)
        for i in range(len(ret)):
            ret[i] = ret[i][:-1]
        return ret