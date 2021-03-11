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

    @staticmethod
    def build(array):
        root = head = ListNode(0)
        for i in array:
            head.next = ListNode(i)
            head = head.next
        return root.next
