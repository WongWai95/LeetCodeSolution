class Solution:
    def reverse(self, x: int) -> int:
        pow2_31 = pow(2, 31)

        if x >= 0:
            str_x = str(x)
            result = int(str_x[::-1])
        else:
            str_x = str(-x)
            result = -int(str_x[::-1])
        if result > pow2_31 - 1 or result < -pow2_31:
            return 0
        else:
            return result
            