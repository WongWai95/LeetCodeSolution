class Solution:
    def simplifyPath(self, path: str) -> str:
        l_path = path.split('/')
        stack = []
        for e in l_path:
            if e == '' or e == '.':
                continue
            elif e == '..':
                try:
                    stack.pop()
                except IndexError:
                    continue
            else:
                stack.append(e)
        if stack == []: return '/'
        res = ''
        for e in stack:
            res += '/' + e
        return res