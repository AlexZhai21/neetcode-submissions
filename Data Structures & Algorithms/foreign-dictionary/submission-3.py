from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #string a is smaller than string b if 
        #1. first letter where they differ is smaller in a than in b
        #2. a is a prefix of b and a.length < b.legnth
        #this means that everything in words must satisfy this
        n = len(words)
        graph = {} #letter -> [] list of letters greater than it

        for w in words:
            for i in w:
                if i not in graph:
                    graph[i] = set()
                    
        for i in range(n-1):
            w1 = words[i]
            w2 = words[i + 1]
            p1, p2 = 0,0
            while p1 < len(w1) and p2 < len(w2):
                if w1[p1] != w2[p2] and w1[p1] not in graph[w2[p2]]: #we know that p1 < p2
                 #if wp2 already had an edge from wp1, then earlier we saw that wp2 is < wp1, which would mean there is a contradiction
                 #NOTE THAT THAT OTHER CONDTION DOES NOT PREVENT CYCLES FROM OCCURING! CYCLES MAY BE LONGER, SO EVEN IF WP1 ISNT IN WP2, THERE MAY ALREADY BE A CYCLE THATS LONGER THAN TWO NODES
                    graph[w1[p1]].add(w2[p2]) #now we know that wp1 < wp2
                    p1 = len(w1)
                    p2 = len(w2)
                    continue  #should exit the loop             
        
                elif w1[p1] == w2[p2]:
                    p1 +=1
                    p2 += 1
                else:
                    return ""
            if len(w2) < len(w1) and p2 == len(w2) and p1 != len(w1): #this meant that a was a prefix of b and thus is smaller
                return "" #only way this if statement should be registered is if wp2 < wp1 and wp2 was a prefix of wp1, 
                #since if they differ at a character, the length conditions woudlnt be met, same ofr if they were the same string, and if a was a preix of b then the length condtioins wouldnt be met either
        #run cycle detection (OR COULD HAVE MAINTAINED A UNION FIND TO CHECK)
        visited = set()
        path = set()
        def dfs(node):
            visited.add(node)
            if node in path:
                return True
            path.add(node)
            for i in graph[node]:
                if dfs(i):
                    return True
            path.remove(node)
            return False
        for i in graph:
            if i not in visited:
                if dfs(i):
                    return ""

        #after that, just run topological sort
        #GRAPH SHOULD HAVE AN ORDERING OF SMALL THING TO OTHER SMALL THING
        in_deg = defaultdict(int)
        der_dek = deque()
        ans = []
        print(graph)
        for i in graph:
            in_deg[i] += 0
            for j in graph[i]:
                in_deg[j] += 1
        print(in_deg)
        for i in in_deg:
            if in_deg[i] == 0:
                der_dek.append(i)
        print(der_dek)
        while der_dek:
            top = der_dek.pop()
            ans.append(top)
            for i in graph[top]:
                in_deg[i] -= 1
                if in_deg[i] == 0:
                    der_dek.append(i)
        return "".join(ans)


                


        
        