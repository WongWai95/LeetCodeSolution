class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        try:
            length1 = min([len(s) for s in strs])
        except:
            length1 = 0
        length2 = len(strs)
        
        for i in range(length1):
            current_char = strs[0][i]
            flag = True
            for j in range(1, length2):
                if not current_char == strs[j][i]:
                    flag = False
                    break
            if flag == True:
                prefix = prefix + current_char
            else:
                break
        return prefix