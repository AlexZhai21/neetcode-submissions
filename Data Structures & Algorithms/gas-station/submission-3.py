class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i] - cost[i] for i in range(len(gas))] #difference betweent he gas and the cost
        left_sum = 0
        right_sum = sum(diff)
        curr_max_expend = left_sum
        curr_max = right_sum
        curr_start = 0
        for i in range(len(diff) - 1):
            left_sum += diff[i]
            right_sum -= diff[i]
            if right_sum > curr_max:
                curr_max = right_sum
                curr_start = i + 1
                curr_max_expend = left_sum
        if curr_max + curr_max_expend >= 0:
            return curr_start
        return -1
#my logic is that you want your possible starting point to be the point wher eyou collect the most amount of gas before you like start your circle. 
#right_sum calculates how mcuh gas you would collect and left_sum is how much you would collect as well but to finish the loop (negative gas means ur expending gas)
#how i came to this was that initially i tried differences and wanted to just find the balance point but this wouldnt work due to the fact that you coud have a situation like 3 -5 1000000, where even though the sum is super positive, starting at the 3 point is a fail since you wouldn't even make it to the 1000000.
#however, with finding the MAX possible amoutn of gas to collect, you would never start at 3 since 100000 + 3 -5 is less than just starting at 100000 straight up.
        