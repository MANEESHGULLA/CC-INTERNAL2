class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BT:
    def __init__(self, val):
        self.root = Node(val)
        self.dia=0

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.val)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val)

    def levelorder(self, root):
        res = []
        q = []

        if not root:
            return res

        q.append(root)

        while q:
            level = []
            n = len(q)

            for i in range(n):
                node = q.pop(0)
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)

        return res

    def zigzagLevelOrder(self, root):
        res = []
        q = []

        if not root:
            return res

        ltor = True
        q.append(root)

        while q:
            n = len(q)
            level = []

            for i in range(n):
                node = q.pop(0)
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if not ltor:
                level.reverse()

            res.append(level)
            ltor = not ltor

        return res

    def rightview(self,root):
      res=[]
      q=[root]
      if not root:
        return res

      while q:
        n=len(q)

        for i in range(n):
          node=q.pop(0)

          if i==n-1:
            res.append(node.val)

          if node.left:
            q.append(node.left)
          if node.right:
            q.append(node.right)

      return res

    def diameterBT(self,root):
      if not root:
        return 0

      lefth=self.diameterBT(root.left)
      righth=self.diameterBT(root.right)

      self.dia = max(self.dia,lefth+righth)

      return 1+max(lefth,righth)

    def diameter(self):
      self.diameterBT(self.root)
      return self.dia

    def balanced(self,root):
      def dfs(root):
        if not root:
          return [True,0]

        left=dfs(root.left)
        right=dfs(root.right)

        balance=(left[0] and right[0] and abs(left[1]-right[1])<=1)

        return [balance,1+max(left[1],right[1])]

      return dfs(root)[0]

    def lowestCommonAncestor(self,root,p,q):
      if not root or root==p or root==q:
        return root

      left=self.lowestCommonAncestor(root.left,p,q)
      right=self.lowestCommonAncestor(root.right,p,q)

      if left and right:
        return root


      return left if left else right




# Create tree
tree = BT(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)




# Traversals
print("Preorder:")
tree.preorder(tree.root)
print("\nInorder:")
tree.inorder(tree.root)
print("\nPostorder:")
tree.postorder(tree.root)
print("\nLevelorder:")
print(tree.levelorder(tree.root))
print("\nZigzag Levelorder:")
print(tree.zigzagLevelOrder(tree.root))
print("\nRightview:")
print(tree.rightview(tree.root))
print("\nDiameter:")
print(tree.diameter())
print("\nbalanced:")
print(tree.balanced(tree.root))
print("\nLowest Common Ancestor:")
node1=tree.root.right
node2=tree.root.left.left
print(tree.lowestCommonAncestor(tree.root,node1,node2).val)

