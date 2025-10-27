#is valid bst
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self, val):
        self.root = Node(val)

    def isValidBST(self,root):
      def helper(low,node,high):
        if not node:
          return True

        if not low<node.val<high:
          return False

        return helper(low,node.left,node.val) and helper(node.val,node.right,high)

      return helper(float('-inf'),root,float('inf'))

tree = BST(5)
tree.root.left = Node(1)
tree.root.right = Node(4)
tree.root.right= Node(6)
tree.root.left.right = Node(3)
tree.root.right.right = Node(7)
print(tree.isValidBST(tree.root))  #True
