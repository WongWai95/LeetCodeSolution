class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        negative = numerator // denominator < 0
        numerator, denominator = abs(numerator), abs(denominator)
        last_leave = numerator % denominator
        res = str(numerator // denominator)
        if negative: res = '-' + res
        if last_leave != 0:
            res += '.'
        else:
            return res
        remainder = {}
        index = len(res) - 1
        while last_leave != 0:
            numerator = last_leave * 10
            last_leave = numerator % denominator
            quotient = numerator // denominator
            if numerator in remainder:
                pos = remainder[numerator] + 1
                res = res[:pos] + '(' + res[pos:]
                res += ')'
                break
            res += str(quotient)
            remainder[numerator] = index
            index += 1
        return res