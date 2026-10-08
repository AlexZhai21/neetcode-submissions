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
        #     print(f"i: {i + 1} left sum:{left_sum} right sum: {right_sum}, currmax: {curr_max}")

        # print(f"FINAL DECISION left sum:{left_sum} right sum: {right_sum}, currmax: {curr_max}")
        if curr_max + curr_max_expend >= 0:
            return curr_start
        return -1

        