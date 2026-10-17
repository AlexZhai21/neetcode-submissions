from collections import deque
class Solution: #O(v^2 + v + e)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #BFS solution
        wordList = [beginWord] + wordList
        seen = set() #space is v
        graph = defaultdict(list) #space is e all edges in the graph
        ans = 0
        for i in range(len(wordList)): #o(n^2)
            wi = wordList[i]
            for j in range(i + 1, len(wordList)):
                wj = wordList[j]
                num_diff = 0
                for k in range(len(beginWord)): #always between 1 to 10 so this is effetively constant
                    if wi[k] != wj[k]:
                        num_diff += 1
                if num_diff == 1: #then there is a path between wi and wj
                    graph[wi].append(wj)
                    graph[wj].append(wi)
        tracker = deque([(1, beginWord)])
        while tracker:

            top = tracker.popleft()
            der_word = top[1]
            level = top[0]
            if der_word == endWord:
                return level
            for i in graph[der_word]:
                if i not in seen:
                    seen.add(i)
                    tracker.append((level + 1, i))
            
        return 0