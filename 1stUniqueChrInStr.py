class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return
        charlist = list(s)
        pair = dict.fromkeys(s, 0)
        while len(charlist) > 0:
            pair[charlist[0]] += 1
            charlist.pop(0)
        for char, charcount in pair.items():
            if charcount == 1:
                return s.index(char)
        return -1

    #     for char in s:
    # if s.index(char) == s.rindex(char):
    #     print(s.index(char))
    #     break
