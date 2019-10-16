class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': 0, ')': 1, '[': 3, ']': 4, '{': 6, '}': 7, 'X': 9}
        remain = ''
        found_flag = False
        if len(s) == 0: return True
        for index in range(1, len(s)):
            if mapping[s[index]] - mapping[s[index-1]] == 1:
                found_flag = True
                s = s[0:index-1] + 'XX' + s[index+1:]
        if found_flag == False:
            return False
        else:
            s = s.replace('X', '')
            return self.isValid(s)