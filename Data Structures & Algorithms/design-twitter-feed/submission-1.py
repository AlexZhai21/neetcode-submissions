import heapq
class Twitter:

    def __init__(self): #use graphs to model who follows who
        self.graph = {} #person: [people they follow]
        self.tweets = {} #person: [(tweet, time)]
        self.time = 0 #how to track order of the tweets
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1 #since heapq is by defualt min heap

    def getNewsFeed(self, userId: int) -> List[int]:
        top_things = self.tweets.get(userId, []).copy()
        # print(f"tweets{self.tweets}")
        # print(f" graph {self.graph}")
        ans = []
        if userId in self.graph:
            for f in self.graph[userId]:
                top_things.extend(self.tweets.get(f, []))
        heapq.heapify(top_things)
        # print(f"top{top_things}")
        for i in range(10):
            if top_things:
                ans.append(heapq.heappop(top_things)[-1])
                print(ans)
            else:
                return ans
        return ans
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId not in self.graph:
            self.graph[followerId] = set()
      
        self.graph[followerId].add(followeeId) #
  

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.graph[followerId]:
            self.graph[followerId].remove(followeeId)
  
        
