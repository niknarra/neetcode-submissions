class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [] # Stack to track directories
        currDir = '' # String to track current directory

        # we add '/' to the end to track the last directory in the path
        for char in path + '/':
            if char == '/':
                # If we encounter a .., pop the previous directory if exists, otherwise move
                if currDir == '..':
                    if stack:
                        stack.pop()
                # Check if currDir is a valid directory
                elif currDir != '' and currDir != '.':
                    stack.append(currDir)
                
                # Reset current directory tracker string
                currDir = ''
            
            else:
                currDir += char
        
        return '/' + '/'.join(stack)
