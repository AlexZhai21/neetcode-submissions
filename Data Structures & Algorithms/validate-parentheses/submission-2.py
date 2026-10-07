class Solution:
    def isValid(self, s: str) -> bool:
        map_track = {")": "(",  "}": "{", "]": "["}
        open_b = []
        for i in s:
            if i not in map_track: #this means its an open bracket
                open_b.append(i)
            else: #this means its a close bracket
                if len(open_b) == 0 or open_b.pop() != map_track[i]:
                    return False
        if len(open_b) == 0:
            return True
        else:
            return False
