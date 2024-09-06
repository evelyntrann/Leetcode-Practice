class Solution
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(":")", "[":"]", "{":"}"}
        open = set(["(", "[", "{"])
        for char in s:
            if char in open:
                stack.append(char) 
            elif stack and char == mapping[stack[-1]]: # check if the value in the mapping match the last append into the stack
                stack.pop() # if there is a match, please delete it 
            else:
                return False
        return not stack #return stack = []
