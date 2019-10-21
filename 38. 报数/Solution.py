class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        origin = self.countAndSay(n-1)
        count = 0
        num = '0'
        res = ''
        for i in range(len(origin)):
            if not origin[i] == num:
                res = res + str(count) + num
                count = 1
                num = origin[i]
            else:
                count += 1
        return res[2:] + str(count) + num