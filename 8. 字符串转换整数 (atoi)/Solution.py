class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        digital = 0
        sign = 1
        
        if str == '':
            return 0
        if len(str) == 1 and (str == '-' or str == '+'):
            return 0
        
        if str[0] == '-':
            sign = -1
            str = str[1:]
        elif str[0] == '+':
            sign = 1
            str = str[1:]
        
        for i in range(len(str)):
            if 0x30 <= ord(str[i]) <= 0x39:
                digital = digital * 10 + int(str[i])
            else:
                break
        
        result = digital * sign
        pow2_31 = pow(2, 31)
        if result > pow2_31 - 1:
            result = pow2_31 - 1
        if result < -pow2_31:
            result = -pow2_31
        
        return result