class Solution:
    def makeGood(self, s: str) -> str:
        codes = list()
        stack = list()
        for char in s:
            codes.append(ord(char))
        for code in codes:
            if stack and abs(stack[-1] - code) == 32:
                stack.pop()
            else:
                stack.append(code)
        for i in range(len(stack)):
            stack[i] = chr(stack[i])
        return "".join(stack)
