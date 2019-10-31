class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            carry_new = (digits[i] + carry) // 10
            digits[i] = (digits[i] + carry) % 10
            carry = carry_new
        if carry == 1:
            digits.insert(0, carry)
        return digits