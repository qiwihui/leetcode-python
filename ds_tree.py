

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.val)
        printTree(node.right, level + 1)

class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        printTree(self)
        return ""
    
def build_from_level_order(arr, root, i, n):

    # Base case for recursion
    if i < n:
        root = TreeNode(arr[i])

        # insert left child
        root.left = build_from_level_order(arr, root.left,
                                     2 * i + 1, n)

        # insert right child
        root.right = build_from_level_order(arr, root.right,
                                      2 * i + 2, n)
    return root
