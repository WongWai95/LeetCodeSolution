class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1 = []
        l2 = []
        for i in range(len(a)-1, -1, -1):
            l1.append(int(a[i]))
        for i in range(len(b)-1, -1, -1):
            l2.append(int(b[i]))
            
        carry = 0
        res = []
        for i in range(min(len(l1), len(l2))):
            res.append((l1[i] + l2[i] + carry) % 2)
            carry = (l1[i] + l2[i] + carry) // 2
        for i in range(min(len(l1), len(l2)), max(len(l1), len(l2))):
            res.append((l1[i]+carry)%2 if len(l1)>len(l2) else (l2[i]+carry)%2)
            carry = (l1[i]+carry)//2 if len(l1)>len(l2) else (l2[i]+carry)//2
        if carry != 0:
            res.append(carry)
        res_str = ''
        for i in range(len(res)-1, -1, -1):
            res_str += str(res[i])
        return res_str