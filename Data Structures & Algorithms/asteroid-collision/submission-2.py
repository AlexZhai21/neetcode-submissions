class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for i in range(len(asteroids)):
            a = asteroids[i]
            if not res:
                res.append(a)
            else:
                
                prev = res[-1] #the previous asteroid
                if prev > 0 and a > 0 or prev < 0 and a < 0 or prev < 0 and a > 0:
                    res.append(a) #going int he same direction and will never meet
                else: #opposite directions -> collision
                    while a and prev and a < 0 and prev > 0:
                        if abs(a) > abs(prev):
                            res.pop() #destroyed that asteroid
                            if res:
                                prev = res[-1]
                            else:
                                prev = None
                        elif abs(a) == abs(prev): #both destroied
                            res.pop()
                            if res:
                                prev = res[-1]
                            else:
                                prev = None
                            a = None
                        else: #if a < prev, a is destroyed
                            a = None
                    if a:
                        res.append(a)
        return res

        