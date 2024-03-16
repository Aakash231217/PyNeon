class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class Trees:
    def __init__(self,root):
        self.root = Node(root)
    def preorder(self,start,records):
        if start is not None:
            records.append(start.value)
            records = self.preorder(start.left,records)
            records = self.preorder(start.right,records)
#Root-> Left Subtree-> Right Subtree
        return records
    def postorder(self,start,records):
        if start is not None:
            records = self.postorder(start.left,records)
            records = self.postorder(start.right,records)
            records.append(start.value)
        return records

tree=Trees(5)
tree.root.left = Node(3)
tree.root.right = Node(4)
tree.root.left.left = Node(2)
tree.root.left.right = Node(8)
tree.preorder(tree.root,[])
print(tree.preorder(tree.root,[]))
print(tree.postorder(tree.root,[]))
#   5
#  / \
# 3   4
#/ \
#2  8