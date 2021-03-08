class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        head = self
        res = []
        while head is not None:
            res.append(str(head.val))
            head = head.next
        return "->".join(res)