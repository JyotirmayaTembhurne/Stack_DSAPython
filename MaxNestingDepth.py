class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        depth = set()
        for char in s:
            if char == "(":
                count += 1
            if char == ")":
                count -= 1
            depth.add(count)
        return max(depth)
        # count = 0
        # max_count = 0
        # for char in s:
        #     if char == "(":
        #         count += 1
        #         max_count = max(max_count, count)
        #     if char == ")":
        #         count -= 1
        # return max_count
