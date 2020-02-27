class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split(' ')
        # print(s)
        s_list = []
        for e in s:
            if e != '':
                s_list.append(e)
        res = ''
        for e in s_list[::-1]:
            res += '{} '.format(e)
        return res[:-1]