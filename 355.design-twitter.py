#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
# https://leetcode.com/problems/design-twitter/description/
#
# algorithms
# Medium (31.41%)
# Likes:    1218
# Dislikes: 227
# Total Accepted:    62.3K
# Total Submissions: 198.3K
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user and is able to see the 10 most recent tweets in
# the user's news feed. Your design should support the following methods:
# 
# 
# 
# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news
# feed. Each item in the news feed must be posted by users who the user
# followed or by the user herself. Tweets must be ordered from most recent to
# least recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
# 
# 
# 
# Example:
# 
# Twitter twitter = new Twitter();
# 
# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
# 
# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);
# 
# // User 1 follows user 2.
# twitter.follow(1, 2);
# 
# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
# 
# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id
# 5.
# twitter.getNewsFeed(1);
# 
# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
# 
# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);
# 
# 
#

# @lc code=start
from typing import List
from queue import PriorityQueue

# global global_timestamp
global_timestamp = 1

class Tweet:
    
    def __init__(self, id, timestamp):
        self.id = id
        self.time = -timestamp
        self.next = None
    
    def __lt__(self, other):
        return self.time <= other.time
    def __le__(self, other):
        return self.time < other.time
    def __eq__(self, other):
        return self.time == other.time
    def __ne__(self, other):
        return self.time != other.time
    def __gt__(self, other):
        return self.time >= other.time
    def __ge__(self, other):
        return self.time > other.time

class User:
    
    def __init__(self, id):
        self.id = id
        self.followers = [self.id]
        self.head: Tweet = None
    
    def post(self, tweet_id):
        global global_timestamp
        tweet = Tweet(tweet_id, global_timestamp)
        global_timestamp += 1
        tweet.next = self.head
        self.head = tweet
    
    def follow(self, user_id):
        if user_id not in self.followers:
            self.followers.append(user_id)
    
    def unfollow(self, user_id):
        if user_id != self.id and user_id in self.followers:
            self.followers.remove(user_id)


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = dict()
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        user = self.users.setdefault(userId, User(userId))
        user.post(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        pq = PriorityQueue()
        user = self.users.get(userId)
        if not user:
            return []
        for follower_id in user.followers:
            f = self.users.get(follower_id)
            if f and f.head:
                pq.put(f.head)
        res = []
        while not pq.empty():
            tweet = pq.get()
            res.append(tweet.id)
            if len(res) >= 10:
                return res
            if tweet.next:
                pq.put(tweet.next)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        follower = self.users.setdefault(followerId, User(followerId))
        self.users.setdefault(followeeId, User(followeeId))
        follower.follow(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        follower = self.users.setdefault(followerId, User(followerId))
        self.users.setdefault(followeeId, User(followeeId))
        follower.unfollow(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

if __name__ == "__main__":
    twitter = Twitter()

    twitter.postTweet(1, 5)
    # print(twitter.getNewsFeed(1))
    print(twitter.getNewsFeed(1) == [5])

    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    # print(twitter.getNewsFeed(1))
    print(twitter.getNewsFeed(1) == [6, 5])

    twitter.unfollow(1, 2)
    # print(twitter.getNewsFeed(1))
    print(twitter.getNewsFeed(1) == [5])
