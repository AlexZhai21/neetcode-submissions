from collections import defaultdict
import heapq
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = [beginWord] + wordList
        seen = set()
        graph = defaultdict(list)
        ans = 0
        for i in range(len(wordList)):
            wi = wordList[i]
            for j in range(i + 1, len(wordList)):
                wj = wordList[j]
                num_diff = 0
                for k in range(len(beginWord)):
                    if wi[k] != wj[k]:
                        num_diff += 1
                if num_diff == 1: #then there is a path between wi and wj
                    graph[wi].append(wj)
                    graph[wj].append(wi)
        #just run dijsktras on this graph
        minHeap = [[0, beginWord]] #want to fidn the shortest distance from beginword to endword
        ans = 0
        while minHeap:
            top = heapq.heappop(minHeap)
            der_word = top[1]
            if der_word in seen:
                continue
            dist = top[0]
            if der_word == endWord:
                ans = dist
                return ans + 1
            for i in graph[der_word]:
                heapq.heappush(minHeap, [dist + 1, i])
            seen.add(der_word)
            
        return 0


            
        


        
        


        