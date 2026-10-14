class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l, r = 0,0
        curr_sum = 0 #thisshouldbethenumberofpeoplehecanconvert
        best_start = [0,0]
        for i in range(minutes):
            curr_sum += customers[r] * grumpy[r]
            r += 1
        best_start[1] = curr_sum
        while r < len(customers):
            curr_sum -= customers[l] * grumpy[l]
            l += 1
            
            curr_sum += customers[r] * grumpy[r]
            if curr_sum > best_start[1]:
                best_start = [l, curr_sum]
            r += 1
        ans = 0
        print(best_start)
        for i in range(len(customers)):
            if i >= best_start[0] and i < best_start[0] + minutes: #hes not grumpy o matter what
                ans += customers[i]
            else:
                ans += customers[i] * (1 -grumpy[i])
        return ans


        