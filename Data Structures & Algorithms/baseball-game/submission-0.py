class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        res = []

        for op in operations:
            if op == '+':
                a, b = res[-1], res[-2]
                res.append(a+b)
            elif op == 'C':
                res.pop()
            elif op == 'D':
                a = res[-1]
                res.append(2*a)
            else:
                res.append(int(op))
        
        return sum(res)