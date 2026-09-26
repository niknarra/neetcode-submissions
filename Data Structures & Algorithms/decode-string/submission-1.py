class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            
            elif char == ']':
                chars = []
                while stack and stack[-1] != '[':
                    chars.append(stack.pop())
                
                if stack:
                    stack.pop()
                
                curr = ''.join(reversed(chars))

                counts = []
                while stack and stack[-1].isdigit(): 
                    counts.append(stack.pop())

                count = int(''.join(reversed(counts)))

                while count > 0:
                    stack.append(curr)
                    count -= 1

        return ''.join(stack)
