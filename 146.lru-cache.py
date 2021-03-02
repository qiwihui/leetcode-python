#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (35.76%)
# Likes:    7885
# Dislikes: 323
# Total Accepted:    712.4K
# Total Submissions: 2M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
# 
# Implement the LRUCache class:
# 
# 
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
# 
# 
# Follow up:
# Could you do get and put in O(1) time complexity?
# 
# 
# Example 1:
# 
# 
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= capacity <= 3000
# 0 <= key <= 3000
# 0 <= value <= 10^4
# At most 3 * 10^4 calls will be made to get and put.
# 
# 
#

# @lc code=start

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoubleList:

    def __init__(self):
        # 头尾虚节点
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        # 元素个数
        self.size = 0
    
    def add_last(self, node: Node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1
    
    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_first(self):
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first

class LRUCache:

    def __init__(self, capacity: int):
        self.map = dict()
        self.cache = DoubleList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.make_recently(key)
        return self.map.get(key).value
        
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.delete(key)
            self.add_recently(key, value)
            return
        if self.capacity == self.cache.size:
            # 删除最久未使用的元素
            self.remove_least_recently()
        self.add_recently(key, value)
    
    def make_recently(self, key):
        """将某个 key 提升为最近使用的"""
        node = self.map.get(key)
        self.cache.remove(node)
        self.cache.add_last(node)

    def add_recently(self, key, value):
        """将某个 key 添加为最近使用的"""
        node = Node(key, value)
        self.cache.add_last(node)
        self.map[key] = node

    def delete(self, key):
        """删除 key"""
        node = self.map.get(key)
        self.cache.remove(node)
        del self.map[node.key]
    
    def remove_least_recently(self):
        """删除最久未使用的元素"""
        node = self.cache.remove_first()
        del self.map[node.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(2, 1)
    lru.put(2, 2)
    lru.get(2)
    lru.put(1, 1)
    lru.put(4, 1)
    lru.get(2)
