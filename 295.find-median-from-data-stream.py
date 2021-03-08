#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (46.91%)
# Likes:    3818
# Dislikes: 72
# Total Accepted:    275.4K
# Total Submissions: 586.1K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# For example,
# 
# [2,3,4], the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Design a data structure that supports the following two operations:
# 
# 
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
# 
# 
# 
# 
# Example:
# 
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 
# 
# 
# Follow up:
# 
# 
# If all integer numbers from the stream are between 0 and 100, how would you
# optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how
# would you optimize it?
# 
# 
#

# @lc code=start
import queue

class PeekablePriorityQueue(queue.PriorityQueue):

    def peek(self):
        """Peeks the first element of the queue
        
        Returns
        -------
        item : object
            First item in the queue
        
        Raises
        ------
        queue.Empty
            No items in the queue
        """
        try:
            with self.mutex:
                return self.queue[0]
        except IndexError:
            raise queue.Empty

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = PeekablePriorityQueue()
        self.large = PeekablePriorityQueue()

    def addNum(self, num: int) -> None:
        if self.small.qsize() >= self.large.qsize():
            self.small.put(num)
            self.large.put(-self.small.get())
        else:
            self.large.put(-num)
            self.small.put(-self.large.get())

    def findMedian(self) -> float:
        if self.small.qsize() > self.large.qsize():
            return self.small.peek()
        elif self.small.qsize() < self.large.qsize():
            return -self.large.peek()
        else:
            return (self.small.peek() - self.large.peek())/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())
    mf.addNum(3)
    print(mf.findMedian())
