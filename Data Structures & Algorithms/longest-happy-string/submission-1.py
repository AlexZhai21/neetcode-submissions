import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = [[-1 * a, "a"], [-1 * b, "b"], [-1 * c, "c"]]
        heapq.heapify(maxHeap)
        inrow = [None, 0]
        ans = []
        banned = None
       
        while maxHeap:
            # print(f"curr answer is {ans}")
            # print(f"curr banned is {banned}")
            # print(f"curr in a row is {inrow}")
            
            top = heapq.heappop(maxHeap)
            count = top[0]
            let = top[1]
            if count == 0:
                continue

        
            if let == inrow[0] and inrow[1] == 2:
                    #can't use this one
                banned = top
                # print(banned)
                continue
            elif let == inrow[0]: #inrow[1] == 1
                ans.append(let)
                inrow[1] = inrow[1] + 1
            else:
                    #this isnt something we used recently
                ans.append(let)
                inrow = [let, 1]
            if banned and inrow[0] != banned[1]: #can use the banned one again
                # print("UNBANNED")
                heapq.heappush(maxHeap, banned)
                banned = None
            top[0] = top[0] + 1
            if top[0] < 0:
                heapq.heappush(maxHeap, top)
        return "".join(ans)



        


            
            