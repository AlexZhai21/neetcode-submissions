class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        n = len(digits)
        der_ans = []
        if not digits:
            return der_ans
        def backtracker(s, i): #i determine what digit we are on, s can be the current string
            if i >= n:
                der_ans.append("".join(s))
                return
            for t in range(len(mapping[digits[i]])):
                s.append(mapping[digits[i]][t])
                backtracker(s, i + 1)
                s.pop()
        backtracker([], 0)
        return der_ans
            




        