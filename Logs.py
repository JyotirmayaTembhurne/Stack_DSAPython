class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = list()
        for action in logs:
            if action != "./" and action != "../":
                stack.append(action)
            if action == "../" and len(stack) != 0:
                stack.pop()
            if action == "./":
                pass
        return len(stack)
