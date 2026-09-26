class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        curr = ''

        for char in path + '/':
            if char == '/':
                if curr == '..':
                    if res:
                        res.pop()
                elif curr != '' and curr != '.':
                    res.append(curr)
                curr = ''

            else:
                curr += char

        return '/'+'/'.join(res)