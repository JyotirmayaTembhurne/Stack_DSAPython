class Solution:
    def minLength(self, s: str) -> int:
        stack = list()
        for char in s:
            if stack and stack[-1] == "A" and char == "B":
                stack.pop()
            elif stack and stack[-1] == "C" and char == "D":
                stack.pop()
            else:
                stack.append(char)
        return len(stack)