class Solution:
    def checkValidString(self, s: str) -> bool:
        left_par = []
        star_par = []
        for i in range(len(s)):
            if s[i] == "(":
                left_par.append(("(", i))
            elif s[i] == "*":
                star_par.append(("*", i))
            else:
                if left_par:
                    left_par.pop()
                elif star_par:
                    star_par.pop()
                else:
                    return False
        if len(left_par) == 0:
            return True
        if len(star_par) == 0:
            return False
        print(left_par)
        print(star_par)
        left_p = 0
        for i in star_par:
            if left_p >= len(left_par):
                return True
            if i[1] > left_par[left_p][1]:
                left_p += 1
        return len(left_par) == left_p


        