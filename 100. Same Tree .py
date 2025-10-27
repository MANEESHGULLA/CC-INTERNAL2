#same tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BT:
    def __init__(self, val):
        self.root = Node(val)

    def isSameTree(self,p,q):
      if not p and not q:
            return True

      if not p or not q or p.val!=q.val:
            return False

      return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)



# Create tree
tree = BT(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)


tree2 = BT(1)
tree2.root.left = Node(2)
tree2.root.right = Node(3)
tree2.root.left.left = Node(4)
tree2.root.left.right = Node(5)

print(tree.isSameTree(tree.root,tree2.root)) #True


