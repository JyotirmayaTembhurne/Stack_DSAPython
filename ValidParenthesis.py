s = s = "({[)]})"


class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")": "(", "]": "[", "}": "{"}
        stack = list()
        for parenthesis in s:
            if parenthesis in pair.values():
                stack.append(parenthesis)
            elif parenthesis in pair.keys():
                if len(stack) == 0 or stack.pop() != pair[parenthesis]:
                    return False
        return len(stack) == 0
