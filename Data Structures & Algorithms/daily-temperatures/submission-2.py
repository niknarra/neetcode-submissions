class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()

            if stack:
                res.append(stack[-1][1] - i)

            else:
                res.append(0)
            
            stack.append((temperatures[i], i))

        
        return res[::-1]