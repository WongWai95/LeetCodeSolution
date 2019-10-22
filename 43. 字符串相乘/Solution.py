class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def multi_one(multi: list, one: int, pos: int) -> list:
            carry = 0
            res = [0 for _ in range(pos)]
            for i in range(len(multi)):
                res.append((multi[i] * one + carry) % 10)
                carry = (multi[i] * one + carry) // 10
            res.append(carry)
            return res
        def plus(l1: list, l2: list) -> list:
            carry = 0
            res = []
            for i in range(min(len(l1), len(l2))):
                res.append((l1[i] + l2[i] + carry) % 10)
                carry = (l1[i] + l2[i] + carry) // 10
            for i in range(min(len(l1), len(l2)), max(len(l1), len(l2))):
                res.append((l1[i]+carry)%10 if len(l1) > len(l2) else (l2[i]+carry)%10)
                carry = (l1[i]+carry)//10 if len(l1) > len(l2) else (l2[i]+carry)//10
            return res
            
        list1 = [int(num1[e]) for e in range(len(num1)-1, -1, -1)]
        list2 = [int(num2[e]) for e in range(len(num2)-1, -1, -1)]
        ret = []
        temp = []
        for i in range(len(list2)):
            temp = multi_one(list1, list2[i], i)
            ret = plus(ret, temp)
        str_res = ''
        flag = False
        while len(ret) > 1 and ret[-1] == 0:
            ret.pop()
        for i in range(len(ret)-1, -1, -1):
            str_res += str(ret[i])
        return str_res