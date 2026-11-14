class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        #main dilemma right now is do we care about maximizing the local weight of people ont he boat
        l = 0
        r = len(people) - 1
        boats = 0
        while l <= r:
            smallus = people[l]
            biggus = people[r]
            if smallus + biggus <= limit:
                l += 1
                r -=1
            else:
                r -=1 #put the big person on the boat
            boats += 1
        return boats