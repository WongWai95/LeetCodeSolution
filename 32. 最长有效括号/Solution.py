class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def find_longest(ss):
            left = -1
            count = 0
            for right in range(len(ss)):
                if ss[right] == 'X':
                    continue
                elif ss[right] == '(':
                    left = right
                else:
                    if not left == -1:
                        ss = ss[0:left] + 'X' + ss[left+1:right] + 'X' + ss[right+1:]
                        left = -1
                        count += 1
            if count == 0:
                return ss
            else:
                return find_longest(ss)
        
        max_len = 0
        length = 0
        proceed_s = find_longest(s)
        print(proceed_s)
        for e in proceed_s:
            if e == 'X':
                length += 1
                max_len = max(max_len, length)
            else:
                length = 0
        return max_len